# -*- coding: utf8 -*-

class MyClass(object):

    def __set_data(self, value):
        self.inner_value = value
        print("Set inner_value to ", self.inner_value)

    def __get_data(self):
        print("Get inner_value as ", self.inner_value)
        return self.inner_value

    def __del_data(self):
        print("Delete inner_value with ", self.inner_value)
        del self.inner_value

    prop = property(fget = __get_data, fset = __set_data, fdel = __del_data)

obj = MyClass()
obj.prop = "obj.prop"

obj2 = MyClass()
obj2.prop = "obj2.prop"

print(obj.prop)
print(obj2.prop)
print(obj.inner_value)
print(obj2.inner_value)