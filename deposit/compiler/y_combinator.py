def y_combinator(gen):
    return (lambda g: g(g))(lambda f: gen(lambda *args: f(f)(*args)))


ret = y_combinator(lambda fab: lambda n: 1 if n < 2 else n * fab(n - 1))(10)
print(ret)


def y_comb(gen):
    return (lambda g: g(g))(lambda f: (lambda *args: (gen(f(f)))(*args)))


ret = y_comb(lambda fab: lambda n: 1 if n < 2 else n * fab(n - 1))(10)
print(ret)

