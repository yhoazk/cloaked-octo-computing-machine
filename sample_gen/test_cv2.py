#!/usr/bin/python
import cv2
import numpy as np

img = cv2.imread('B5.png')
rows,cols,chan = img.shape

"""
scale

M = np.float32([[1,0,100],[0,1,50]])
res = cv2.resize(img,None,fx=8, fy=8, interpolation = cv2.INTER_CUBIC)
"""


"""
rotate
M = cv2.getRotationMatrix2D((cols/2,rows/2),-5,1)
dst = cv2.warpAffine(img,M,(cols,rows))
"""

"""
Translate
"""
res = cv2.resize(img,None,fx=.85, fy=.85, interpolation = cv2.INTER_CUBIC)
M = np.float32([[1,0,10],[0,1,5]])
dst = cv2.warpAffine(res,M,(cols,rows))
print dst.shape




cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
