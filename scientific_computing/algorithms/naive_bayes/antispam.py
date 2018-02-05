#coding=utf-8
import numpy as np


class AntiSpam:
    def __init__(self):
        self.wc = {}
        self.mc = {}

    def incw(self, word, category):
        self.wc.setdefault(word, {})
        self.wc[word].setdefault(category, 0)
        self.wc[word][category] += 1

    def incm(self, category):
        self.mc.setdefault(category, 0)
        self.mc[category] += 1

    def train(self, words, category):
        for w in words:
            self.incw(w, category)
        self.incm(category)

    def show(self):
        print("mc: %s \nwc:%s\n\n\n" % (self.mc, self.wc))

    def wcount(self, word, category):
        if word in self.wc and category in self.wc[word]:
            return float(self.wc[word][category])
        return 1.0

    def wprob(self, word, category):
        return self.wcount(word, category) / self.mc[category]

    def cprob(self, category):
        return float(self.mc[category]) / sum(self.mc.values())

    def safe_prob(self, words):
        s, h = 0.0, 0.0
        for w in words:
            s += np.log(self.wprob(w, 'spam'))
            h += np.log(self.wprob(w, 'health'))
        s += np.log(self.cprob('spam'))
        h += np.log(self.cprob('health'))
        return np.exp(s) / (np.exp(s) + np.exp(h))

    def prob(self, words):
        sprob, hprob = 1.0, 1.0
        for w in words:
            sprob *= self.wprob(w, 'spam')
            hprob *= self.wprob(w, 'health')
        sprob *= self.cprob('spam')
        hprob *= self.cprob('health')
        return sprob / (sprob + hprob)


antiSpam = AntiSpam()
for i in range(4989):
    antiSpam.train(['hello', 'world', 'todo'], 'health')

for k in range(4901):
    antiSpam.train(['invoice', 'bill', 'todo'], 'spam')

antiSpam.train(['discount', 'promotion', 'cool'], 'health')
for k in range(10):
    antiSpam.train(['spam', 'mail', 'attention'], 'health')

for k in range(9):
    antiSpam.train(['discount', 'promotion', 'cool'], 'spam')

for k in range(90):
    antiSpam.train(['spam', 'mail', 'attention'], 'spam')

antiSpam.show()

print('P(discount,spam,todo)={0}'.format(antiSpam.prob(['discount', 'spam', 'todo'])))
print('P(discount,spam,todo)={0}'.format(antiSpam.safe_prob(['discount', 'spam', 'todo'])))

print('P(hello,mail,todo)={0}'.format(antiSpam.prob(['hello', 'mail', 'todo'])))
print('P(hello,mail,todo)={0}'.format(antiSpam.safe_prob(['hello', 'mail', 'todo'])))

print('P(invoice,discount,bill)={0}'.format(antiSpam.prob(['invoice', 'discount', 'bill'])))
print('P(invoice,discount,bill)={0}'.format(antiSpam.safe_prob(['invoice', 'discount', 'bill'])))
