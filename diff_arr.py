# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
test = 123123
s_tst = str(test)
it = iter(s_tst)
n = next(it)
l = []
n1 = n
for e in range(len(s_tst)):
    try:
       # print(n
        print("{} - {} = {}".format(n1,n,int(n1)-int(n)))
        l.append(int(n1)- int(n))
        n = next(it)
        n1 = next(it)
       # print(n1)
    except StopIteration:
        print("Done")
        break

print(l)
