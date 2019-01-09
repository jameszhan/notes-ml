
class MyClass(object):
    def __init__(self):
        self.x = 11
        self.y = [1, 2, 3]
        
    def method(self):
        pass
    x = 10
    y = []

obj = MyClass()

[print("obj.__dict__[{}] = {}".format(k, v)) for k, v in obj.__dict__.items()]
[print("MyClass.__dict__[{}] = {}".format(k, v)) for k, v in MyClass.__dict__.items()]