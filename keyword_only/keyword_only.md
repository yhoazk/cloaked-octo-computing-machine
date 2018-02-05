# Keyword Only Arguments

In python there is a way to specify that certain paramters to a 
function, must be specified along with the keyword, otherwise the 
call will fail. 

## Example:

```python
def foo(a,b,*,c,d):
    print(a,b,c,d)

foo(1,2,3,4)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-f8f8c2cc1d9c> in <module>()
----> 1 foo(1,2,3,4)

TypeError: foo() takes 2 positional arguments but 4 were given
```

For this method the correct signature is:

```python
foo(1,2,c=3,d=4)
```

Here another example where all the elements must be specified:

```python
def bar(*,x,y,z):
    print(x+y+z)
```
The last method can be called only with this signature:
```python
bar(x=3,y=5,z=9)
17
```
