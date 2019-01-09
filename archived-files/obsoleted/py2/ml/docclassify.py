#coding=utf-8
import re
import math


class classifier:
    def __init__(self, getfeatures, filename = None):
        # 统计特征/分类组合的数量
        self.fc = {}
        # 统计每个分类中的文档数量
        self.cc = {}
        self.getfeatures = getfeatures

    # 增加对特征/分类组合的计数值
    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1

    # 增加对某一分类的计数值
    def incc(self, cat):
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1

    # 某一特征出现于某一分类中的次数
    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    # 属于某一分类的内容项数量
    def catcount(self, cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    # 所有内容项的数量
    def totalcount(self):
        return sum(self.cc.values())

    # 所有分类的列表
    def categories(self):
        return self.cc.keys()

    def train(self, item, cat):
        features = self.getfeatures(item)
        for f in features:
            self.incf(f, cat)
        self.incc(cat)

    def fprob(self, f, cat):
        count = self.fcount(f, cat)
        catcount = self.catcount(cat)
        print("f: ", f, "cat: ", cat, "count: ", count, ", catcount: ", catcount)
        if count != 0:
            return count / catcount
        else:
            return 0

    def weightedprob(self, f, cat, prf, weight=1.0, ap=0.5):
        # 计算当前的概率
        basicprob = prf(f, cat)
        # 统计特征在所有分类出现的次数
        totals = sum([self.fcount(f, c) for c in self.categories()])
        # 计算加权平均
        return ((weight * ap) + totals * basicprob) / (weight + totals)


class naivebayes(classifier):
    def __init__(self, getfeatures):
        classifier.__init__(self, getfeatures)
        self.thresholds = {}

    def setthresholds(self, cat, v):
        self.thresholds[cat] = v

    def getthresholds(self, cat):
        if cat not in self.thresholds:
            return 1.0
        else:
            return self.thresholds[cat]

    def docprob(self, item, cat):
        features = self.getfeatures(item)
        p = 1
        for f in features:
            p *= self.weightedprob(f, cat, self.fprob)
        return p

    def prob(self, item, cat):
        catprob = self.catcount(cat) / self.totalcount()
        docprob = self.docprob(item, cat)
        return docprob * catprob

    def classify(self, item, default=None):
        probs = {}
        maxprob = 0.0
        best = None
        for cat in self.categories():
            probs[cat] = self.prob(item, cat)
            if probs[cat] > maxprob:
                maxprob = probs[cat]
                best = cat

        for cat in probs:
            if cat == best:
                continue
            elif probs[cat] * self.getthresholds(best) > probs[best]:
                return default
            return best


def getwords(doc):
    splitter = re.compile('\\W*')
    words = [s.lower() for s in splitter.split(doc) if len(s) > 1 and len(s) < 20]
    return dict([(w, 1) for w in words])


classifier = naivebayes(getwords)

classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")
classifier.train("my name is lily", "bad")

classifier.train("my name is james", "bad")
classifier.train("my name is ad", "good")
classifier.train("my name is python", "good")
classifier.train("my name is ruby", "good")
classifier.train("hello the world, hahaha, good time", "bad")
classifier.train("a, b, c, d, e, f, g", "good")

classifier.fprob("my", "good")
classifier.fprob("my", "bad")


print(classifier.prob("my name is lily", "good"))
print(classifier.prob("my name is lily", "bad"))
print(classifier.classify("my name is lily"))

print(classifier.prob("my name is luck", "good"))
print(classifier.prob("my name is luck", "bad"))
print(classifier.classify("my name is luck"))