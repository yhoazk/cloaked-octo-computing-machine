#!/usr/bin/env python

import numpy as np
import pickle
from PIL import Image
import sys
import math
import base64
from matplotlib import pyplot as plt
#http://placekitten.com/200/300
img = Image.open("127b.bmp").convert('L') # open and convert to BW
bts = np.fromstring(img.tobytes(), dtype=np.uint8)

o=pickle.dumps({"a":[1,2,3,4], "cdrrrr":21323.333, "np":np.ones(1984)*5.64, "pi":math.pi, "fnc":math.sqrt})
btso = np.fromstring(o,dtype=np.uint8)
#d=int(math.sqrt(sys.getsizeof(o)))
d=int(math.sqrt(btso.size))
print(bts.size)
print(btso.size)
##
print(bts.shape)
print(btso.shape)
bb = bts + btso
Image.frombytes(mode='1', size=(d,d), data=bb).save("img.bmp")
Image.frombytes(mode='1', size=(d,d), data=img.tobytes()).save("img_bts.bmp")
