# cloaked-octo-computing-machine
Experimental_Python


**Linear Regression**

Example of how to make linear regression in python using scipy


**Pickle**

Stores python objects in files.
Useful to save processed data or training coefs for CNNs.

Note: Files generated with pickle for python 3 are not backward compatible for python 2.7

**Sample Generator**
Useful to generate more samples to train CNNs.



### How to solve the error in anaconda 

> This application failed to start because it could not find or load the Qt platform plugin "xcb"
>in "".
> 
>Reinstalling the application may fix this problem.
>Abortado ('core' generado)


As the message says we need to reinstall the program, the issue here is which program we need to reinstall.
This are the commands we need to run in order to fix this bug:

```
sudo /opt/anaconda3/bin/conda remove qt
sudo /opt/anaconda3/bin/conda remove pyqt
sudo /opt/anaconda3/bin/conda install qt
sudo /opt/anaconda3/bin/conda install pyqt
```

## Notes 

### ternary operator:
```python
t="10" if 4 < 5 else "22"
```


#### References in python

Here is an example on how python hides memory:
```python
def dict_modifier(d, key):
  d.pop(key, None)

sample_dict = {'some_key': 'some value'}
dict_modifier(sample_dict, 'some_key')
print(sample_dict)  # {}
```

The function `dict_modifier` removes a value form the dictionary passed to it, it handles the dictionary as a reference.
But python not always takes the arguments as references for example:
```python
def adder(n):
  n += 1

i = 1
adder(i)
print(i)  # 1
```
The primitives are **not** passed as references, but rather as copies.

#### Compile a python script for correctness
```
python -m py_compile xpad_diag_helper.py
```

#### Get import paths
[https://stackoverflow.com/questions/5751292/how-to-get-current-import-paths-in-python](https://stackoverflow.com/questions/5751292/how-to-get-current-import-paths-in-python)

The path locations that python cheks by default can be inspected in sys.path.

```python
import sys
print sys.path
```
