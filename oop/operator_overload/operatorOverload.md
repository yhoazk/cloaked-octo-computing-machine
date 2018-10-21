# Operator Overload

[List](https://docs.python.org/3/reference/datamodel.html#special-method-names)

In Python, as almos anything is an object, these entities have already defined
methods, to overload their behaviour when they are used with different operators
is just a matter of implement a specific function call.

## constructor `__init__()`:

This "overloads" how the object is initialized.

## Convert to string `__str__()`:

This changes how an object is converted to string.

## Arithmetic

* `__add__(self, other)`: addition : `+`
* `__sub__(self, other)`: subtraction : `-`
* `__mul__(self, other)`: multiplication : `*`
* `__matmul__(self, other)`: matmul : `@` TODO:
* `__truediv__(self, other)`: division : `/`
* `__floordiv__(self, other)`: floor div : `\\`
* `__mod__(self, other)`: modulo : `%`
* `__divmod__(self, other)`: divmod : ``
* `__pow__(self, other)`: power : `**`
* `__lshift__(self, other)`: left shift : `<<`
* `__rshift__(self, other)`: right shift : `>>`
* `__and__(self, other)`:  and : `&`
* `__xor__(self, other)`:  xor : `^`
* `__or__(self, other)`: or : `|`




To implement "swapped" operations the functions are different:

* `object.__radd__(self, other)`
* `object.__rsub__(self, other)`
* `object.__rmul__(self, other)`
* `object.__rmatmul__(self, other)`
* `object.__rtruediv__(self, other)`
* `object.__rfloordiv__(self, other)`
* `object.__rmod__(self, other)`
* `object.__rdivmod__(self, other)`
* `object.__rpow__(self, other)`
* `object.__rlshift__(self, other)`
* `object.__rrshift__(self, other)`
* `object.__rand__(self, other)`
* `object.__rxor__(self, other)`
* `object.__ror__(self, other)`

## Comparisons:

* `__lt__()`: less than : `<`
* `__le__()`: less or equal : `<=`
* `__eq()__`: equal to : `==`
* `__ne__()`: not equal : `!=`
* `__gt__()`: greater than : `>`
* `__ge__()`: greater than or eqal : `>=`




## Example:


```Python
import math
 
class Circle:

    def __init__(self, radius):
        self.__radius = radius
    def setRadius(self, radius):
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return math.pi * self.__radius ** 2
    def __add__(self, another_circle):
        return Circle( self.__radius + another_circle.__radius )
    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius
    def __str__(self):
        return "Circle with radius " + str(self.__radius)
c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2
print(c3.getRadius())
print( c3 > c2) # Became possible because we have added __gt__ method
print( c1 < c2) # Became possible because we have added __lt__ method
print(c3) # Became possible because we have added __str__ method

```

For Classes and any object in order to be callable, the metod `__call__` must
be implemented. This is useful when usign python decorators.