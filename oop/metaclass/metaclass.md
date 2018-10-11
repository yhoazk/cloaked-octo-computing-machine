# Python metaclasses

As we already know, everything in python is an object. This means is the instance
of a class. This includes classes too. In python classes are first-class objects.
They can be createdd at runtime, passed and returned from functions and assigned
to variables.

`type` is itself a metaclass.

metaclasses are used as a class factory, however metaclasses define a type of a
class, not just a factory for it. Because of this it's possible to define normal
methods in the metaclass, these metaclass methods are like class methods in that
they cannot be called on an instance of the class.


## `__new__` vs `__init__`

- - -

https://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/