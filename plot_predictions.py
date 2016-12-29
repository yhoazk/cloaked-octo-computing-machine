# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:27:03 2016

@author: uidw7238
"""

import pickle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

def getData():
    data  = pickle.load(open("./train.p","rb"))
    
    return data['features'], data['labels']


#def plot_signs(imgs):

def get_TopK(np_arr):
    """
    Returns the top 5 elements
    """
    list_arr =  list(np_arr)
    return list_arr[:-5]

    

img, labels = getData()
label_list = labels.tolist()
class_count = []
for n in range(labels.max() + 1):
    print("Class: " + str(n) + "  Num of items: " + str(label_list.count(n)))
    class_count.append(label_list.count(n))
        
    
plt.bar(range(len(class_count)), class_count)

plt.show()

#--------------------------

x = range(5)
x_v = np.asarray([random.uniform(0,1) for i in x])
colours = ['red','blue','green','yellow', 'magenta']


f, arrx = plt.subplots(10,2, figsize=(15,20), gridspec_kw = {'width_ratios':[7, 2]})

for n, sb_plt in enumerate(arrx):
    
    sb_plt[0].imshow(img[n], extent=[0,200,0,1], aspect=200)
    sb_plt[0].set_title("Guess")
    sb_plt[0].axis('off')
    sb_plt[1].bar(x, x_v, tick_label=['Tom', 'Dick', 'Harry', 'Slim', 'Jim'], color='red')
    sb_plt[1].set_title("Confidence")
    
    
plt.tight_layout()
plt.show()




