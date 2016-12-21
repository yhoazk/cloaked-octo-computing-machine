#!/usr/bin/python
"""
Example of the library pickle to store
python objects and restore them again
w/o processing them
"""

import pickle
import numpy as np



"""
Define objects to store
"""

npTest_obj = np.asarray([[1,2,3],[6,5,4],[8,7,9]])

strTest_obj = "pickle example XXXX"




if __name__ == "__main__":
    # store object information
    pickle.dump(npTest_obj, open("npObject.p", "wb"))
    pickle.dump(strTest_obj, open("strObject.p", "wb"))

    # read information from file
    str_readObj = pickle.load(open("strObject.p","rb"))
    np_readObj = pickle.load(open("npObject.p","rb"))
    print(str_readObj)
    print(np_readObj)
