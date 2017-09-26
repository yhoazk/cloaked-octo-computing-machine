# Class Methods
[src](https://realpython.com/blog/python/instance-class-and-static-methods-demystified/)
There are 3 different types of class methods for a class:
- "Regular"
- class
- static 

For example the demo class:
```python
class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
```
## Regular methods
This are the basic method type used most of the times. This methods take
at least one parameter `self`, which points to an instance of `myClass`
when the method is called.

Through the `self` parameter, instance methods can freely access attributes
and other methods on the same object, this gives them a lot if power when
it comes to modifying an object's state.

Not only can they modify object state, instance methods can also access the
class itself through the `self.__class__` attribute. This means instance
methods can also modify class state.

> >>> obj = MyClass()
> >>> obj.method()
> ('instance method called', <MyClass instance at 0x101a2f4c8>)


Here Python replaces the `this` with a pointer to the instance.
The above snippet is the same as:
> obj = myClass()
> myClass.method(obj)

## Class Methods
This methods instead of accepting a `self` parameter, class methods take
a `cls` parameter that points to the class -- and not the object instance--
 when the method is called.

Because the class method can only access to this `cls` argument, it can't
modify object instance state. That would require access to `self`. 
However, class methods can still modify class state that applies accross 
all instnaces of the class.

## Static Methods

This type of methods takes neither `self` nor a `cls` parameter, but it
can accept an arbitray set of other parameters.

## Example of an "useful" case

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
>>> Pizza(['cheese', 'tomato'])
Pizza(['cheese', 'tomato'])
```

In order to generate a [factory](https://en.wikipedia.org/wiki/Factory_(object-oriented_programming%29) for our class:

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
```

Nothe how is used the `cls` argument is the `margherita` and `prosciutto`
factory methods instead of calling the `Pizza` constructor directly.

This is a trick you can use to follow the `Dont repeat yourself(DRY)`
principle. This way is we rename the class at any point in the future
we won't have to update all the calls.



As python only allows one `__init__` method per class, use class methods
to add as many alternative constructors as necessary. This can make the
interface for your classes self-documenting and symplify its usage.


### When to use static methods



