# Python @property

[Source](https://www.programiz.com/python-programming/property)
`@property` is the pythonic way to use getters and setters.

Lets suppose a simple class `Celsius`

```python
class Celsius:
    def __init__(self, temp = 0):
        self.temperature = temp

    def to_f(self):
        return (self.temperature * 1.8)+32
```

To use the objects from the class `Celsius`
can do as follows:


```python
>>> test = Celsius() # create a new object
>>> # set value
>>> test.temperature = 23 
>>> test.temperature # access the value
>>> test.to_f() # use the value in the class
```
When we assing or retreive any object like `temperature`
Python searches in the Object's `_dict__` dictionary.

```python
>>> test.__dict__
{'temperature' : 37}
```

Then internally `test.temperature` becomes `test.__dict__['temperature']`

Now supposing that we need to add the restriction in which it is not 
allowed to set a temperature less than -273 degrees, which is also called
absolute zero.

The obvious way to implement this would be to implement a function to set
and get the value and make `temperature` a private attribute as follows:

```python
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_f(self):
        return (self.get_temperature() * 1.8) + 32
    
    ## needed implementation
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        self._temperature = value
    
```


The variable `temperature` was replaced by `_temperature`, in python
this denotes private variables.

The modification to the class implements the restriction, but the
way to access the attribute, now has to be modified and this turns
to be not backward compatible, and anyone using it must replace the
calls.

```python
>>> c = Celsius(-277)
Traceback (most recent call last):
...
ValueError: Temperature below -273 not possible
>>> test = Celsius() # create a new object
>>> # set value
>>> test.set_temperature(23)
>>> test.get_temperature() # access the value
>>> 
```

# @property

To solve the problem there's the `property` class.

```python
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_f(self):
        return (self.get_temperature() * 1.8) + 32
    
    ## needed implementation
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        self._temperature = value

    temperature = 

```
