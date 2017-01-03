#!/bin/python3
#https://www.hackerrank.com/contests/101hack38/challenges/points-on-a-line

import sys


n = int(input().strip())
lx =[]
ly =[]
for a0 in range(n):
    x,y = input().strip().split(' ')
    ly.append(int(y))
    lx.append(int(x))
    

if len(set(ly)) == 1 or len(set(lx)) == 1:
    print("YES")
else:
    print("NO")
