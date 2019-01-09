# -*- coding: utf-8 -*-


def backtrack(n, check, handle):
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
    backtrack(n, check, lambda a: print([l[a[i]] for i in range(n)]))


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True
    backtrack(n, check, lambda a: print(a))


print("permutation(['A', 'B', 'C'])")
permutation(['A', 'B', 'C'])

print("\nnqueen(4)")
nqueen(4)
