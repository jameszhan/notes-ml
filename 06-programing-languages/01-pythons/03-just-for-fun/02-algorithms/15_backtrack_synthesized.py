# -*- coding: utf-8 -*-


def display(a):
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    print([l[a[i]] for i in range(len(a))])


def backtrack_recursive(n, m, check, handle):
    def dfs(a, k):
        for i in range(n):
            a[k] = i
            if check(a, k):
                if k == m - 1:
                    handle(a)
                else:
                    dfs(a, k + 1)
    a = [0 for _ in range(m)]
    dfs(a, 0)


def backtrack_iterative(n, m, check, handle):
    k, a = 0, [-1 for _ in range(m)]
    while k >= 0:
        a[k] += 1
        while a[k] < n and not check(a, k):
            a[k] += 1
        if a[k] == n or k == m:
            k -= 1
        else:
            if k == m - 1:
                handle(a)
            else:
                k += 1
                a[k] = -1


backtrack = backtrack_iterative


def counter(n, m):
    backtrack(n, m, lambda a, k: True, lambda a: print(a))


def permutation(n, m):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True
    backtrack(n, m, check, display)


def combination(n, m):
    def check(a, k):
        for i in range(k):
            if a[i] >= a[k]:
                return False
        return True
    backtrack(n, m, check, display)


def nqueen(n):
    def check(a, k):
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True
    backtrack(n, n, check, lambda a: print(a))


def deep_first_search(g):
    def check(a, k):
        if k == 0:
            return True
        for i in range(k):
            if a[i] == a[k]:
                return False
        for i in range(k - 1, -1, -1):
            if g[a[i]][a[k]] == 1:
                return True
        return False

    def dfs(n, check, handle):
        k, a = 0, [-1 for i in range(n)]
        while k >= 0:
            a[k] += 1
            while a[k] < n and not check(a, k):
                a[k] += 1
            if a[k] == n:
                k -= 1
            else:
                if k == n - 1:
                    handle(a)
                else:
                    k += 1
                    a[k] = -1
    n = len(g)
    dfs(n, check, display)


graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

if __name__ == '__main__':

    print("counter =>")
    counter(6, 3)

    print("permutation =>")
    permutation(6, 3)

    print("combination =>")
    combination(6, 3)

    print("nqueen =>")
    nqueen(4)

    print("paths =>")
    deep_first_search(graph)
