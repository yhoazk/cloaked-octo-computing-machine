# -*- encoding utf-8 -*-
#!/usr/env python
""" Example for a wrapper class extending and handling a sub-class
"""


class att_dic:
    att1 = dict()
    att2 = list()


    def method1(self,a,b):
        return a+b

    def only_base(self):
        print("Only base")

class Wrapper(object):
    '''
    Object wrapper class.
    This a wrapper for objects. It is initialiesed with the object to wrap
    and then proxies the unhandled getattribute methods to it.
    Other classes are to inherit from it.
    '''
    def __init__(self, obj):
        '''
        Wrapper constructor.
        @param obj: object to wrap
        '''
        # wrap the object
        self._wrapped_obj = obj

    def __getattr__(self, attr):
        # see if this object has attr
        # NOTE do not use hasattr, it goes into
        # infinite recurrsion
        if attr in self.__dict__:
            # this object has it
            return getattr(self, attr)
        # proxy to the wrapped object
        return getattr(self._wrapped_obj, attr)

    def method1(self,a,b):
        return a-b


def main():
    base = att_dic()
    test  = Wrapper(base)
    test.only_base()
    print(test.method1(10,50))


if "__main__" == __name__:
    main()
