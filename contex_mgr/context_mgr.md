# [Python with Context Managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)

Given that garbage collected languages are not suitable for the implementation of
destructors, as there is no guarantee that they will be called, python way of
ensure or handle resource leak or lock is context management.

The `with` statement is useful when two related operatios need to be run as a
pair. The common use case is open a file:

```python
with open("out.txt", "w") as f:
    f.write("text")
```

The `with` statement above will automatically close the file when leaving the
nested block of code. It's guaranteed to close the file no matter how the block
is leaved, even if an exception occurs. In that case the file will close the
file before the exception is caught by an outer exception handler.

To implement the behaviour of the context manager two methods are defined:
`__enter__` and `__exit__`. 

- - -

## Resource Management in garbage collected languages
<br>[src](https://eklitzke.org/resource-management-in-gc-languages)<br>

