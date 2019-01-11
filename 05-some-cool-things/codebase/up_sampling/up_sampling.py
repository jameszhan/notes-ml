# -*- coding: utf-8 -*-

import numpy as np
import re
import itertools
import logging
from decimal import Decimal

logger = logging.getLogger("UpSampling")

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

units = '(?:十|百|千|万|兆)?' \
        '(?:只|次|大卡|张|对开张|转|年|月|天|小时|分钟|秒|克|毫克|吨|米|厘米|毫米|微米|平方米|立方米|平方厘米|立方厘米|寸|英寸' \
        '|座|毫升|升|瓦|马力|伏安|伏|度|摄氏度|开尔文|赫兹|帕斯卡|帕|分特|元|美元|岁|周岁' \
        '|r|min|h|Gbq|kg|g|mg|t|㎞|㎝|㎜|μm|km|cm|mm|㎡|m³|m2|m3|㎝2|㎝3|cm2|cm3' \
        '|ml|l|cc|kw|w|va|kva|kv|v|℃|hz|PPM|KPa|MPa|Pa|m|°|%|‰)' \
        '(?:/(?:分钟|分|小时|时|立方米|立方厘米|平米|平方米|平方厘米|吨|kg|h|min|m|s|㎡|m³|m2|m3|㎝2|㎝3|cm2|cm3))?'

gt_pattern = re.compile('＞|>|大于|超过|以上', re.U)
ge_pattern = re.compile('≥|>=|大于等于|不小于|及以上', re.U)
lt_pattern = re.compile('<|＜|小于|以下', re.U)
le_pattern = re.compile('≤|<=|小于等于|不大于|不超过|及以下', re.U)
eq_pattern = re.compile('=|等于', re.U)

regexes = [
    r'(?P<lower>[\d.]+)\s*[-~到－]\s*(?P<upper>[\d.]+)(?P<unit>(?:{0}))'.format(units),
    r'(?P<lower>[\d.]+)(?P<unit>(?:{0}))\s*[-~到－]\s*(?P<upper>[\d.]+)(?P=unit)'.format(units),
    r'(?P<lower>[\d.]+)\s*(?P<op>＜|<|≤|<=)\s*(?P<unit>(?:{0}))\s*(?P<op2>＜|<|≤|<=)(?P<upper>[\d.]+)'.format(units),
    r'(?P<upper>[\d.]+)\s*(?P<op>＞|>|≥|>=)\s*(?P<unit>(?:{0}))\s*(?P<op2>＞|>|≥|>=)(?P<lower>[\d.]+)'.format(units),
    r'(?P<lower>[\d.]+)\s*(?P<unit>(?:{0}))\s*(?P<op>＜|<|≤|<=)\s*(?P<prefix>[^\d≥＞>]+)\s*(?P<op2>＜|<|≤|<=)'
    r'(?P<upper>[\d.]+)(?P=unit)'.format(units),
    r'(?P<upper>[\d.]+)\s*(?P<unit>(?:{0}))\s*(?P<op>＞|>|≥|>=)\s*(?P<prefix>[^\d≤＜<]+)\s*(?P<op2>＞|>|≥|>=)'
    r'(?P<lower>[\d.]+)(?P=unit)'.format(units),
    r'(?P<lower>[\d.]+)\s*(?P<op>＜|<|≤|<=)\s*(?P<prefix>[^\d≥＞>]+)\s*(?P<op2>＜|<|≤|<=)(?P<upper>[\d.]+)'
    r'(?P<unit>(?:{0}))'.format(units),
    r'(?P<upper>[\d.]+)\s*(?P<op>＞|>|≥|>=)\s*(?P<prefix>[^\d≤＜<]+)\s*(?P<op2>＞|>|≥|>=)(?P<lower>[\d.]+)'
    r'(?P<unit>(?:{0}))'.format(units),
    r'(?P<op>＞|>|大于|超过|<|＜|小于|≥|>=|大于等于|不小于|≤|<=|小于等于|不大于|不超过|=|等于)(?P<num>[\d.]+)(?P<unit>(?:{0}))'.format(units),
    r'(?P<num>[\d.]+)(?P<unit>(?:{0}))(?P<op>及以下|以下|以上|及以上)'.format(units)
]

range_patterns = []
for regex in regexes:
    range_patterns.append(re.compile(regex, re.U | re.I))


def do_search(text, patterns, index):
    matcher = None
    for pattern in patterns:
        m = pattern.search(text, index)
        if m:
            if matcher is None or matcher.start() > m.start():
                matcher = m
    return matcher


def match(s, patterns):
    items = []
    index = 0
    s_len = len(s)
    while True:
        m = do_search(s, patterns, index)
        if m:
            start, end = m.span()
            if start > index:
                items.append(s[index:start])
            if end > start:
                items.append(m.groupdict())
            index = end
        else:
            break
    if s_len > index:
        items.append(s[index:s_len])
    return items


def _generate_range(lower, upper, lower_included, upper_included):
    lower_v = Decimal(lower)
    upper_v = Decimal(upper)
    lower_exponent = lower_v.as_tuple()[2]
    upper_exponent = upper_v.as_tuple()[2]
    if lower_exponent > upper_exponent:
        exponent = upper_exponent
    else:
        exponent = lower_exponent
    candidates = []
    if lower_included:
        candidates.append(lower_v)
    step = Decimal(str(round(10 ** exponent, -exponent)))
    if lower_v + step == upper_v:
        step = step / 10
    v = lower_v
    while v < upper_v:
        v += step
        if v < upper_v:
            candidates.append(v)
    if upper_included:
        candidates.append(upper_v)
    return candidates


def generate_range(lower, upper, lower_included, upper_included):
    logger.debug('generate_range with {0}.'.format((lower, upper, lower_included, upper_included)))
    if lower.isdigit() and upper.isdigit():
        lower_v = int(lower)
        upper_v = int(upper)
        if lower_v % 1000 == 0 and upper_v % 1000 == 0:
            step = 1000
        elif lower_v % 500 == 0 and upper_v % 500 == 0:
            step = 500
        elif lower_v % 100 == 0 and upper_v % 100 == 0:
            step = 100
        elif lower_v % 50 == 0 and upper_v % 50 == 0:
            step = 50
        elif lower_v % 10 == 0 and upper_v % 10 == 0:
            step = 10
        elif lower_v % 5 == 0 and upper_v % 5 == 0:
            step = 5
        else:
            step = 1

        if (upper_v - lower_v) / step < 5:
            if step == 1000 or step == 500 or step == 100 or step == 50 or step == 10:
                step = int(step / 10)
            elif step == 5:
                step = 1
            else:
                step = 0.5

        if not lower_included:
            lower_v += step
        if upper_included:
            upper_v += step
        if step >= 1:
            return range(lower_v, upper_v, step)
        else:
            return np.arange(lower_v, upper_v, step)
    else:
        return _generate_range(lower, upper, lower_included, upper_included)


def do_generate(d):
    if 'op' not in d:
        lower = d['lower']
        upper = d['upper']
        unit = d['unit']
        return ['{0}{1}'.format(v, unit) for v in generate_range(lower, upper, True, True)]
    elif 'op' in d and 'num' in d:
        op = d['op']
        num = d['num']
        unit = d['unit']
        gt_pattern_match = gt_pattern.fullmatch(op)
        ge_pattern_match = ge_pattern.fullmatch(op)
        lt_pattern_match = lt_pattern.fullmatch(op)
        le_pattern_match = le_pattern.fullmatch(op)
        eq_pattern_match = eq_pattern.fullmatch(op)

        if gt_pattern_match or ge_pattern_match:
            lower = num
            if unit == '%':
                upper = '100'
            elif unit == '‰':
                upper = '1000'
            else:
                if num.isdigit():
                    upper = str(int(num) * 4)
                else:
                    upper = str(Decimal(num) * 4)

            r = generate_range(lower, upper, ge_pattern_match, True)
            return ['{0}{1}'.format(v, unit) for v in r]
        elif lt_pattern_match or le_pattern_match:
            upper = num
            lower = '0'
            r = generate_range(lower, upper, False, le_pattern_match)
            return ['{0}{1}'.format(v, unit) for v in r]
        elif eq_pattern_match:
            return ['{0}{1}'.format(num, unit)]
        else:
            logger.warning("Unknown {0}.".format(d))
    elif 'op2' in d:
        lower = d['lower']
        upper = d['upper']
        unit = d['unit']
        op = d['op']
        op2 = d['op2']
        r = generate_range(lower, upper, le_pattern.fullmatch(op) or ge_pattern.fullmatch(op2),
                           le_pattern.fullmatch(op2) or ge_pattern.fullmatch(op))
        if 'prefix' in d:
            return ['{0}{1}{2}'.format(d['prefix'], v, unit) for v in r]
        else:
            return ['{0}{1}'.format(v, unit) for v in r]
    logger.warning("Unknown {0}.".format(d))
    return []


def generate(text):
    candidates = []
    items = match(text, range_patterns)
    if len(items) <= 1:
        return [text]
    else:
        for item in items:
            if type(item) == str:
                candidates.append([item])
            else:
                candidates.append(do_generate(item))
    samples = itertools.product(*candidates)
    return [''.join(sample) for sample in samples]


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('{0} source_file'.format(sys.argv[0]))
        sys.exit(0)

    source_file = sys.argv[1]
    samples_file = source_file + '.samples'

    processed = total = 0
    with open(source_file, 'r', encoding='UTF-8') as source:
        with open(samples_file, 'w', encoding='UTF-8') as output:
            for line in source.readlines():
                total += 1
                generated_texts = generate(line.strip())
                if generated_texts and len(generated_texts) > 1:
                    processed += 1
                    for generate_text in generated_texts:
                        output.write(generate_text)
                        output.write('\n')

    logger.info("Total: {0}, Processed: {1}.".format(total, processed))