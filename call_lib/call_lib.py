#!/usr/bin/python


import ctypes

so_file = "./clib/clib.so"
external_so = ctypes.CDLL(so_file)


# For non trivial functions is necessary to specify
# the type of arguments

external_so.fill_array.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_char, ctypes.c_int)

# create the array TYPE
arr_t = ctypes.c_char * 10
# Create an instance of the array type and override the name
arr_t = arr_t()

# pre-fill the array
for n in range(len(arr_t)):
    arr_t[n] = '#'


print("Array original contents")


for s in arr_t:
    print(s)
print("Call external function")
arr = external_so.fill_array(arr_t, 'x', 9)

print("New contents of the array")
for x in arr_t:
    print(x)

print(type(external_so))
print(external_so.square(10))
print(external_so.square(12))
