#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def script_path():
    return os.path.dirname(__file__)


def make_sift(img):
    sift_obj = cv2.xfeatures2d.SIFT_create()
    descr, kpts = sift_obj.detectAndCompute(img, None)
    return (descr, kpts)

def show(img, title="Img"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


## From OpenCV w/o undestanding the process:
def ez_stitch(img_list):
    stitcher = cv2.Stitcher_create()
    status, stitched = stitcher.stitch(img_list)
    return stitched if status is 0 else None

if __name__ == "__main__":
    print("With OpenCV built in:")
    stitch_dir = script_path() + "/../imgs/stitch/"
    imgs = os.listdir(stitch_dir)
    imgs.sort()
    to_stitch = []
    for img in imgs:
        to_stitch.append(cv2.imread(stitch_dir + img))
    show(ez_stitch(to_stitch))

    img = cv2.imread(script_path() + "/../imgs/" + "sample0.jpg")
    show(img, "original")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show(img, "B&W")

    d, k = make_sift(img)
    print(d)