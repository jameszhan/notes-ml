# -*- coding: utf-8 -*-

import numpy as np

print np.zeros.__doc__
print np.shape.__doc__
print np.concatenate.__doc__


# 创建矩阵
a = np.array([[1, 2, 3], [4, 5, 6]])
print 'a.shape = {0}, a = {1}, type = {2}'.format(a.shape, a, type(a))

b = np.arange(15)
print 'b.shape = {0}, b = {1}'.format(b.shape, b)

c = b.reshape(3, 5)
print 'c.shape = {0}, c = {1}'.format(c.shape, c)

d = np.zeros((5, 3))
print 'd.shape = {0}, d = {1}'.format(d.shape, d)

e = np.ones((5, 3))
print 'e.shape = {0}, e = {1}'.format(e.shape, e)


# 基础操作
print 'b.reshape(5, 3) + e = {0}'.format(b.reshape(5, 3) + e)
print 'dot(e, c) = {0}, dot(c, e) = {1}'.format(np.dot(e, c), np.dot(c, e))
print 'dot(arrange(5), arrange(5).reshape(5, 1)) = {0}'.format(np.dot(np.arange(5), np.arange(5).reshape(5, 1)))

print 'dir(a) = {0}'.format([item for item in dir(a) if not item.startswith('__')])

# 常用属性
print 'a.dtype = {0}, b.dtype = {1}, c.dtype = {2}'.format(a.dtype, b.dtype, c.dtype)
print 'a.ndim = {0}, b.ndim = {1}, c.ndim = {2}'.format(a.ndim, b.ndim, c.ndim)     # 维度
print 'a.size = {0}, b.size = {1}, c.size = {2}'.format(a.size, b.size, c.size)     # 元素数量
print 'a.itemsize = {0}, b.itemsize = {1}, c.itemsize = {2}'.format(a.itemsize, b.itemsize, c.itemsize) #每一个元素所占字节数
print 'a.nbytes = {0}, b.nbytes = {1}, c.nbytes = {2}'.format(a.nbytes, b.nbytes, c.nbytes) # 总字节数 （size * itemsize）
print 'a.real = {0}, b.real = {1}, c.real = {2}'.format(a.real, b.real, c.real)     # 所有元素实数部分
print 'a.imag = {0}, b.imag = {1}, c.imag = {2}'.format(a.imag, b.imag, c.imag)     # 所有元素虚数部分
print 'a.flat = {0}, b.flat = {1}, c.flat = {2}'.format(a.flat, b.flat, c.flat)     # 变成一维(iterator实现)
print 'a.T = {0}, b.T = {1}, c.transpose() = {2}'.format(a.T, b.T, c.transpose())     # 矩阵转置，同transpose()

# 常用方法
print 'a.tolist() = {0}, b.tolist() = {1}, c.tolist()  = {2}'.format(a.tolist(), b.tolist(), c.tolist())     # 转化为原生数组
print 'a.item(5) = {0}, a.item(1, 1) = {1}'.format(a.item(5), a.item(1, 1))         # 获取某一位置元素
print 'a.max() = {0}, b.min() = {1}, c.sum() = {2}'.format(a.max(), b.min(), c.sum())
print 'a.prod() = {0}, a.cumprod() = {1}, c.cumsum() = {2}'.format(a.prod(), a.cumprod(), c.cumsum())
print 'a.all() = {0}, b.any() = {1}, c.mean() = {2}'.format(a.all(), b.any(), c.mean())
print 'a.flatten() = {0}, b.flatten() = {1}, c.flatten() = {2}'.format(a.flatten(), b.flatten(), c.flatten())     # 复制一个一维数组出来

print a
print a.swapaxes(0, 1)  # 将n个维度中任意两个维度进行调换
print a

print a.resize(1, 6)    # 同reshape()，直接在原对象上进行修改
print a

