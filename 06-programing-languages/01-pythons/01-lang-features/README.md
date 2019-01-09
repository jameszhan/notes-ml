# Python 语言特性

## Python 2 与 Python 3 兼容性问题

### `print`

python 2 中 `print` 是一个关键字，有专门的 `print` 语句。

```lex
print_stmt ::= "print" ([expression ("," expression)* [","]]
                | ">>" expression [("," expression)+ [","]])
```

在 Python 2 当中，如下写法都是可以的。

```python
print "Hello World"
print("Hello World")
```

在 Python 3 中，`print` 只是一个内建函数而已。

```python
print("Hello World")
```

### `__future__`

Python 3 出来的时候，Python 的设计者们当然也考虑过代码之间的兼容问题。许多为为兼容性设计的功能可以通过 `__future__` 这个包来导入。

#### 使用 Python 3 的 `print` 函数，禁用 Python 2 的 `print` 语句

```python
from __future__ import print_function
```

#### 像 Python 3 一样，字符串字面量的类型为 Unicode

```python
from __future__ import unicode_literal
```

#### `PEP 328` Imports: 多行导入和绝对/相对导入

```python
from __future__ import absolute_import
```

#### 像 Python 3 一样，整除除整数得到浮点数

```python
from __future__ import division
```