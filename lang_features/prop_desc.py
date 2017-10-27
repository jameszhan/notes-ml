#!/usr/bin/env python

#propertiy is a build-in descriptor

class host(object):
    #wrap so some data so you can't see them ^_^
    def __get_data(self):
        return self.hidden

    def __set_data(self, value):
        self.hidden = value
        #raise AttributeError

    def __del_data(self):
        del self.hidden

    the_prop = property(fget = __get_data,
                        fset = __set_data,
                        fdel = __del_data)


#see i can do anything with my the_prop
h_ins = host()
h_ins.the_prop = 1
h_ins.the_prop = 'string'

print h_ins.the_prop
    
