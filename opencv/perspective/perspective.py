#!/usr/bin/env python

"""
compute the perspective trasnform M, given soruce and destination points
M = cv2.getPerspectiveTransform(src, dst)

Compute the inverse perspective transform
Minv = cv2.getPerspectiveeTransform(dst, src)

Warp a image using perspective transform M
warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_LINEAR)

undistort image
cv2.undistort()
"""



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


"""
Answer from uda
import pickle
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read in the saved camera matrix and distortion coefficients
# These are the arrays you calculated using cv2.calibrateCamera()
dist_pickle = pickle.load( open( "wide_dist_pickle.p", "rb" ) )
mtx = dist_pickle["mtx"]
dist = dist_pickle["dist"]

# Read in an image
img = cv2.imread('test_image2.png')
nx = 8 # the number of inside corners in x
ny = 6 # the number of inside corners in y

# MODIFY THIS FUNCTION TO GENERATE OUTPUT 
# THAT LOOKS LIKE THE IMAGE ABOVE
def corners_unwarp(img, nx, ny, mtx, dist):
    # Pass in your image into this function
    # Write code to do the following steps
    # 1) Undistort using mtx and dist
    img = cv2.undistort(img, mtx, dist)
    # 2) Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 3) Find the chessboard corners
    res, corners = cv2.findChessboardCorners(img_gray, (nx,ny))
    if res == True:
    # 4) If corners found: 
        print(corners.shape)
        src = np.asarray(corners, dtype=np.float32)
        print(src[0][0])
        print(src[nx-1][0])
        print(src[nx*ny-1][0])
        print(src[-(ny-1)][0])
        # a) draw corners
        cv2.drawChessboardCorners(img, (nx,ny), corners, res)
        # b) define 4 source points src = np.float32([[,],[,],[,],[,]])
        src = np.float32([src[0], src[nx-1], src[(nx*ny-1)], src[-(nx)]])
                 #Note: you could pick any four of the detected corners 
                 # as long as those four corners define a rectangle
                 #One especially smart way to do this would be to use four well-chosen
                 # corners that were automatically detected during the undistortion steps
                 #We recommend using the automatic detection of corners in your code
            # c) define 4 destination points dst = np.float32([[,],[,],[,],[,]])
        dst = np.float32([[100,100],[1100, 100],[1100,900],[100,900]])
            # d) use cv2.getPerspectiveTransform() to get M, the transform matrix
        M = cv2.getPerspectiveTransform(src,dst)
        warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR)
            # e) use cv2.warpPerspective() to warp your image to a top-down view
    #delete the next two lines
    return warped, M

top_down, perspective_M = corners_unwarp(img, nx, ny, mtx, dist)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
f.tight_layout()
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=50)
ax2.imshow(top_down)
ax2.set_title('Undistorted and Warped Image', fontsize=50)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

"""
