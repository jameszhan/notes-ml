# -*- coding: utf-8 -*-

def backtrack_recursive(a, k, check, handle):
    n = len(a)
    for i in range(n):
        a[k] = i
        if check(a, k):
            if k == n - 1:
                handle(a)
            else:
                backtrack_recursive(a, k + 1, check, handle)


def backtrack_iterative(n, m, check, handle):
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




def permutation(l, m):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True
    n = len(l)
    backtrack_iterative(n, m, check, lambda a: print([l[a[i]] for i in range(len(a))]))


print("permutation(['A', 'B', 'C', 'D'], 2)")
permutation(['A', 'B', 'C', 'D'], 2)


def combination(l, m):
    def check(a, k):
        for i in range(k):
            if(a[i] >= a[k]):
                return False
        return True
    n = len(l)
    backtrack_iterative(n, m, check, lambda a: print([l[a[i]] for i in range(len(a))]))


print("\ncombination(['A', 'B', 'C', 'D'], 2)")
combination(['A', 'B', 'C', 'D'], 2)


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True
    backtrack_recursive([0 for i in range(n)], 0, check, lambda a: print(a))


print("\nnqueen(4)")
nqueen(4)
