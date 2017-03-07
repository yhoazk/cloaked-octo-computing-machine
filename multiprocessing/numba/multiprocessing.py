#!/usr/bin/env python
# -*- coding: utf-8 -*-


import itertools as it
import numpy as np
#from numba import jit
from timeit import default_timer as timer
from multiprocessing import Pool


wmod = np.array([[0,1,2],[3,4,5],[6,7,3]])
pmod = np.array([[0,1,2],[3,4,5],[6,7,3]])

plines1 = it.product(wmod[0],wmod[1],wmod[2])
plines2 = it.product(pmod[0],pmod[1],pmod[2])

print(dir(plines2))
check = .915
result = []
#@jit
def test(A, B, check = .915):
    global result
    res = (np.sum(B)+10)/(np.sum(A)+12)
    if test > check:
        result.append(res,[A,B])

if __name__ == "__main__":
    s = timer()
    for count, (A,B) in enumerate(zip(plines1,plines2)):
        pass

        test = (np.sum(B)+10)/(np.sum(A)+12)
        if test > check:
            result = np.append(result,[A,B])

    print('No multiprocessing results: ',result)
    e = timer()
    print(e - s)
    
    s = timer()
    p = Pool(7)
    p.map(test,[zip(plines1,plines2)])
    print('No multiprocessing results: ',result)
    e = timer()
    print(e - s)
