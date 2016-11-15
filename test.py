"""conditional assignment"""

# http://stackoverflow.com/questions/101268/hidden-features-of-python
y = 1
x=3 if(y == 0) else 2 ## assigns 2 to x

print [(i,j) for i in range(3) for j in range(i)]


def fnc():
  global y
  return 3 if y==0 else 2
 
class C(object):
  def __getitem__(self, item):
  return item
  
C()[1:2, ..., 3]
(slice(1, 2, None), Ellipsis, 3)
  
  
fnc()
