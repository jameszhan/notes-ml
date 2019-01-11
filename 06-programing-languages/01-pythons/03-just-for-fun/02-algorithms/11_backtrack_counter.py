# -*- coding: utf-8 -*-


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


print("counter(6, 3, lambda x: print(x))")
counter(6, 3, lambda x: print(x))
