import collections

print(id("Hello World!"))
print(type(()), type([]), type({}), type(1), type("1"))
print("dir()")
print(dir())
print("dir(collections)")
print(', '.join(dir(collections)))
print("dir(dict)")
print(', '.join(dir(dict)))
help("keywords")
help("obj")
#print(callable(id))
print(hasattr(id, '__call__'), hasattr(dir, '__call__'), hasattr(dir(), '__call__'))
print(isinstance(1, int), isinstance(int, int), isinstance(int, type), isinstance((), tuple))



r = range(1, 10)
print(r)
print(vars({"a": 1, "b": 3, "c": 6}))
