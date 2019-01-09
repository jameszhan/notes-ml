# -*- coding: utf-8 -*-

_str = 'cddeeeffffgggggaaaaaabbbbbbb'
_uni = unicode(_str)
_list = list(_str)
_tuple = tuple(_str)
_bytearray = bytearray(_str)
_buf = buffer(_str)


print 'str = {0}, unicode = {1}, list = {2}, tuple = {3}, bytearray = {4}, buffer = {5}'\
    .format(_str, _uni, _list, _tuple, _bytearray, _buf)
print 'str * 2 = {0}, unicode * 2 = {1}, list * 2 = {2}, tuple * 2 = {3}, bytearray * 2 = {4}, buffer * 2 = {5}' \
    .format(_str * 2, _uni * 2, _list * 2, _tuple * 2, _bytearray * 2, _buf * 2)
print '2 * str = {0}, 2 * unicode = {1}, 2 * list = {2}, 2 * tuple = {3}, 2 * bytearray = {4}, 2 * buffer = {5}' \
    .format(2 * _str, 2 * _uni, 2 * _list, 2 * _tuple, 2 * _bytearray, 2 * _buf)

print 'str[10] = {0}, unicode[10] = {1}, list[10] = {2}, tuple[10] = {3}, bytearray[10] = {4}, buffer[10] = {5}' \
    .format(_str[10], _uni[10], _list[10], _tuple[10], _bytearray[10], _buf[10])
print 'str[7:12]={0}, unicode[7:12]={1}, list[7:12]={2}, tuple[7:12]={3}, bytearray[7:12]={4}, buffer[7:12]={5}' \
    .format(_str[7:12], _uni[7:12], _list[7:12], _tuple[7:12], _bytearray[7:12], _buf[7:12])
print 'str[1:20:3]={0},unicode[1:20:3]={1},list[1:20:3]={2},tuple[1:20:3]={3},bytearray[1:20:3]={4},buffer[1:20:3]={5}'\
    .format(_str[1:20:3], _uni[1:20:3], _list[1:20:3], _tuple[1:20:3], _bytearray[1:20:3], _buf[1:20:3])
print 'len(str)={0}, len(unicode)={1}, len(list)={2}, len(tuple)={3}, len(bytearray)={4}, len(buffer)={5}' \
    .format(len(_str), len(_uni), len(_list), len(_tuple), len(_bytearray), len(_buf))
print 'min(str)={0}, min(unicode)={1}, min(list)={2}, min(tuple)={3}, min(bytearray)={4}, min(buffer)={5}' \
    .format(min(_str), min(_uni), min(_list), min(_tuple), min(_bytearray), min(_buf))
print 'max(str)={0}, max(unicode)={1}, max(list)={2}, max(tuple)={3}, max(bytearray)={4}, max(buffer)={5}' \
    .format(max(_str), max(_uni), max(_list), max(_tuple), max(_bytearray), max(_buf))
print 'str.index(b)={0}, unicode.index(b)={1}, list.index(b)={2}, tuple.index(b)={3}, bytearray.index(b)={4}'\
    .format(_str.index('b'), _uni.index('b'), _list.index('b'), _tuple.index('b'), _bytearray.index('b'))
print 'str.count(b)={0}, unicode.count(b)={1}, list.count(b)={2}, tuple.count(b)={3}, bytearray.count(b)={4}' \
    .format(_str.count('b'), _uni.count('b'), _list.count('b'), _tuple.count('b'), _bytearray.count('b'))

print 'str + unicode + buffer = {0}'.format(_str + _uni + _buf)
print 'list + list = {0}'.format(_list + _list)

print 'a in str => {0}'.format('a' in _str)
print 'a in list => {0}'.format('a' in _list)
print 'a in unicode => {0}'.format('a' in _uni)
print 'a in tuple => {0}'.format('a' in _tuple)
print 'a in bytearray => {0}'.format('a' in _bytearray)
print 'a in buffer => {0}'.format('a' in _buf)

print 'a not in str => {0}'.format('a' not in _str)
print 'a not in list => {0}'.format('a' not in _list)
print 'a not in unicode => {0}'.format('a' not in _uni)
print 'a not in tuple => {0}'.format('a' not in _tuple)
print 'a not in bytearray => {0}'.format('a' not in _bytearray)
print 'a not in buffer => {0}'.format('a' not in _buf)

_range = range(0, 9, 3)
_xrange = xrange(0, 9, 3)


def intersection(list1, list2):
    return [x for x in list1 if x in list2]


def intersect(*lists):
    target = []
    for i, l in enumerate(lists):
        if i == 0:
            target = l
        else:
            target = intersection(target, l)
    return target


print 'range(8) = {0}, range(2, 7) = {1}, range(5, 30, 5) = {2}'.format(range(8), range(2, 7), range(5, 30, 5))
print 'range(9, 0, -1) = {0}, range(0) = {1}, range(1, -1) = {2}'.format(range(9, 0, -1), range(0), range(1, -1))

print 'map(lambda n: 2 * n - 1, [1, 2, 3, 4, 5]) = {0}'.format(map(lambda n: 2 * n - 1, [1, 2, 3, 4, 5]) )
print 'reduce(lambda r, i: r + i, [1, 2, 3, 4, 5], 11) = {0}'.format(reduce(lambda r, i : r + i, [1, 2, 3, 4, 5], 11))


print filter(lambda x: x > 3, range(10))

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
print zip(x, y, z)