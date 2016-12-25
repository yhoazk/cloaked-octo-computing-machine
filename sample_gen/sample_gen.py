#!/usr/bin/python


from __future__ import print_function
import cv2
import numpy as np
import sys
import pickle
import matplotlib.pyplot as plt
import math
import glob
import random


train_imgs=np.asarray([])

def getImages():
    data_set = pickle.load(open("./traffic-signs-data/train.p", "rb"))
    return data_set['features'], data_set['labels']

def loadImgs(path_dir='./', type='png'):
    img_path = glob.glob(path_dir + '/*.'+ type)
    read_imgs = []
    for n in img_path:
        read_imgs.append(cv2.imread(n))
    print("Numer of images read: " + str(len(read_imgs)))
    return read_imgs

def plotImages(img_list):
    x = range(0,10)
    y = range(0,10)
    arr_size = int(math.ceil(math.sqrt(len(img_list))))
    f, arr = plt.subplots(arr_size, arr_size)

    for n, fig in enumerate(arr.reshape(-1)):
        if(n < len(img_list)):
            fig.imshow(img_list[n])

        else:
            #fig.axis('off')
            pass
        fig.axis('off')
    plt.show()


def rotate(img, deg):
    M = cv2.getRotationMatrix2D((img.shape[0]/2,img.shape[1]/2),deg,1)
    dst = cv2.warpAffine(img,M,(img.shape[0],img.shape[1]))
    return dst

def scale(img, deg):
    pass


def translate(img,x,y):
    M = np.float32([[1,0,x],[0,1,y]])
    g = cv2.resize(img,None,fx=.8, fy=.8, interpolation = cv2.INTER_CUBIC)
    return cv2.warpAffine(g,M,(img.shape[0],img.shape[1]))

def shear(img, slant):
    pass


def equalize(img):
    # Std normalization
    #return cv2.equalizeHist(img)
    # adaptive normalization
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(img)

def main(image_path):
    #train_imgs, labels = getImages() FOR useful python 3
    loaded_imgs = loadImgs('./DefinedTS/img', 'png')
    mod_imgs = []
    for n,img in enumerate(loaded_imgs[:10]):
        #Ensure that the rotation is not zero
        for _ in range(10):
            mod_imgs.append(translate(img, random.choice(range(2,10)), random.choice(range(2,10))))



    for n,img in enumerate(mod_imgs):
        for _ in range(10):
            mod_imgs[n] = rotate(img, ((random.randint(7,27))+1) *random.choice([-1,1]) )

    plotImages(mod_imgs)
    #plotImages(loaded_imgs[:4])

    #img = cv2.imread(image_path, 0)
    #cv2.imshow(img, img.shape)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    main(sys.argv[1])
