# -*- coding: utf-8 -*-

print(callable.__doc__)

print(callable([]))
print(callable(()))
print(callable({}))
print(callable(""))
print(callable(False))
print(callable(6))
print(callable(dir))
print(callable(callable.__sizeof__))