#!/usr/bin/python




import numpy as np
from pprint import pprint

"""my_data = [
        ["one", "ein", "uno"],
        ["two", "zwei", "dos"],
        ["three", "drei", "tres"],
        ["four", "vier", "cuatro" ],
        ["five", "funf", "cinco"],
        ["six", "sechs", "seis"] ]

"""
# test data
my_data = np.asarray([
        [1, 2, 3],
        [5, 6, 4],
        [4, 7, 5],
        [3, 8, 6],
        [2, 9, 7],
        [1, 9, 8] ])
#test one hot encoded labels
my_labels = np.asarray([[ 1.,  0.,  0.,  0.,  0.,  0.],
             [ 0.,  1.,  0.,  0.,  0.,  0.],
             [ 0.,  0.,  1.,  0.,  0.,  0.],
             [ 0.,  0.,  0.,  1.,  0.,  0.],
             [ 0.,  0.,  0.,  0.,  1.,  0.],
             [ 0.,  0.,  0.,  0.,  0.,  1.]])

def shuffle_data_labels(data, labels):
    if len(data) != len(labels):
        print("Length must be the same")
        return (None, None)
    else:
        mask = np.random.choice(len(data), 2, replace=False) # here change 5 for the batch size
        data = data[mask]
        labels = labels[mask]
    return(data, labels)


print("Data Before shuffling")
pprint(my_data)
pprint(my_labels)
my_data1, my_labels1 = shuffle_data_labels(my_data, my_labels)
print(my_data1)
print(my_labels1)
print("Data After shuffling")
my_data2, my_labels2 = shuffle_data_labels(my_data, my_labels)
print(my_data2)
print(my_labels2)
print("Data After shuffling")




my_data3, my_labels3 = shuffle_data_labels(my_data, my_labels)
print(my_data3)
print(my_labels3)
print("Data After shuffling")
my_data4, my_labels4 = shuffle_data_labels(my_data, my_labels)
print(my_data4)
print(my_labels4)
print("Data After shuffling")
