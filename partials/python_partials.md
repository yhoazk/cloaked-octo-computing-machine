# Python Partials


Python partials make a new version of a functions with one or more
arguments already filled in (set). It's like a labmda but in a 
pythonic way<sup>1</sup>

```python
sum = lambda x,y : x+y
sum(3,2)
5

incr = lamda y :sum(1,y)
incr(3)
4
def sum2(x,y):
  return y+x

incr2 = functools.partial(sum2, 1)
incr2(4)
5
```

The biggest difference is that lambdas are limited to be a single expression,
while partials can be extended. Another limitation of lambdas; they cannot be
examined using `introspection` and they do not support `@decorators`.






<sub>[1] https://stackoverflow.com/questions/3252228/python-why-is-functools-partial-necessary</sub>

