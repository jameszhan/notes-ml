# -*- coding: utf-8 -*-
import re


def to_human(num):
    p = re.compile('(?<=\d)(?=(\d{3})+$)')
    return p.sub(',', str(num))


print(to_human(1234567890))
print(to_human(123456789))
print(to_human(12345678))
print(to_human(1234567))
print(to_human(123456))
print(to_human(12345))
print(to_human(1234))
print(to_human(123))
print(to_human(12))
print(to_human(1))
