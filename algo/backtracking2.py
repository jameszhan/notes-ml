# -*- coding: utf-8 -*-
from __future__ import print_function


def counter(n, m, handle):
    def track(a, k):    
        for i in range(n):
            a[k] = i
            if k == len(a) - 1:
                handle(a)
            else:
                track(a, k + 1)
    a = [0 for _ in range(m)]
    track(a, 0)


print("\n\n\ncounter(5, 3, lambda a: print(a))")
counter(5, 3, lambda a: print(a))


def backtracking(a, k, check, handle):
    n = len(a)
    for i in range(n):       
        a[k] = i
        if check(a, k):
            if k == n - 1:
                handle(a)
            else:
                backtracking(a, k + 1, check, handle)


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True
    backtracking([0 for i in range(n)], 0, check, lambda a : print(a))


print("\n\n\nnqueen(4)")
nqueen(4)


def permutation(l):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True
    backtracking([0 for i in range(len(l))], 0, check, \
                 lambda a : print([l[a[i]] for i in range(len(a))]) )


print("\n\n\npermutation(['A', 'B', 'C'])")
permutation(['A', 'B', 'C'])



    
