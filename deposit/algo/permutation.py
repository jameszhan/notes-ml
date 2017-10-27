# -*- coding: utf-8 -*-

cnt = 0


def permutation(l, m):
    global cnt
    cnt = 0

    def check(a, k, m):
        for i in range(k):
            if a[i] == a[k]:
                return False
        return True

    def backtrack(m, check):
        global cnt
        k, a, n = 0, [-1 for _ in range(m)], len(l)
        while k >= 0:
            a[k] += 1
            while a[k] < n and not check(a, k, m):
                a[k] += 1
            if a[k] >= n or k >= m:
                k -= 1
            else:
                if k == m - 1:
                    cnt += 1
                    print([l[a[i]] for i in range(m)])
                else:
                    k += 1
                    a[k] = -1

    backtrack(m, check)
    return cnt


if __name__ == '__main__':
    items = ['A', 'B', 'C', 'D', 'E']
    print 'permutation({0}, 2) => {1}'.format(items, permutation(items, 2))
    print 'permutation({0}, 3) => {1}'.format(items, permutation(items, 3))
    print 'permutation({0}, 4) => {1}'.format(items, permutation(items, 4))
    print 'permutation({0}, 5) => {1}'.format(items, permutation(items, 5))


