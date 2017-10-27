# -*- coding: utf-8 -*-
from __future__ import print_function


def backtracking(n, check, handle):
    k, a = 0, [-1 for i in range(n)]
    while k >= 0:
        a[k] += 1
        while a[k] < n and (not check(a, k)):
            a[k] += 1
        if a[k] == n:
            k -= 1
        else:
            if k == n - 1:
                handle(a)
            else:
                k += 1
                a[k] = -1   


def permutation(l):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True
    n = len(l)
    backtracking(n, check, lambda a : print([l[a[i]] for i in range(n)]))


print("\n\n\npermutation(['A', 'B', 'C'])")
permutation(['A', 'B', 'C'])


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True
    backtracking(n, check, lambda a : print(a))


print("\n\n\nnqueen(4)")
nqueen(4)


def backtracking2(n, m, check, handle):
    k, a = 0, [-1 for i in range(m)]
    while k >= 0:
        a[k] += 1
        while a[k] < n and (not check(a, k)):
            a[k] += 1
        if a[k] == n or k == m:
            k -= 1
        else:
            if k == m - 1:
                handle(a)
            else:
                k += 1
                a[k] = -1


def permutation2(l, m):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True
    n = len(l)
    backtracking2(n, m, check, lambda a : print([l[a[i]] for i in range(len(a))]))


print("\n\n\npermutation2(['A', 'B', 'C', 'D'], 2)")
permutation(['A', 'B', 'C'])


def combination(l, m):
    def check(a, k):
        for i in range(k):
            if(a[i] >= a[k]):
                return False
        return True
    n = len(l)
    backtracking2(n, m, check, lambda a:print([l[a[i]] for i in range(len(a))]))


print("\n\n\ncombination(['A', 'B', 'C', 'D'], 2)")
combination(['A', 'B', 'C', 'D'], 2)
