#!/usr/bin/env python

"""

"""
list_l = [ 0,1,2,3,4,5]
U = 3 # shift amount
U = U % len(list_l)
q = list_l[-U:] + list_l[:-U]
print("list before" + str(list_l))
print("list after" + str(q))

