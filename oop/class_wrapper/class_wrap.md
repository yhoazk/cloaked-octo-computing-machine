# Class wrapper

This is an example for the use case where we want to extend or overwrite
an existing object and add functionality (more methods or att) and we
don't have the src.


## Example:

The object `base` contains a set of methods and attributes for a configuration.
If the configuration is faulty or innexistent, the wrapper handles the 
call and sets a different value and returns that value.


### References:
[https://stackoverflow.com/questions/1443129/completely-wrap-an-object-in-python](https://stackoverflow.com/questions/1443129/completely-wrap-an-object-in-python)
[http://code.activestate.com/recipes/577555-object-wrapper-class/](http://code.activestate.com/recipes/577555-object-wrapper-class/)
