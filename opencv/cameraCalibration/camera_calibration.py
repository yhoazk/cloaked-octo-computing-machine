#!/usr/bin/env python


import cv2
import matplotlib.pyplot as plt
import numpy as np

# Image properties
nx = 6 # number of inside corners in x
ny = 9 # number of inside corners in y


if __name__ == "__main__":
    img = cv2.imread("pattern2.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray_img, (nx,ny), None)
    if ret == True:
#Draw and displaythe corners
        cv2.drawChessboardCorners(img, (nx,ny), corners, ret)
        plt.imshow(img)
        plt.show()
    else:
        print("Error", ret, corners)
