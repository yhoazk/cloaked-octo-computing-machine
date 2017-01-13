#!/usr/bin/python


#import sys
#import os

"""
For this the first strategy that comes to mind is to
calculate the distance on each point to all the locker
points, then select the shortest and print it.
"""

# dist |(x0 - xp)|+|(y0 - yp)|
def getMinDist(row, col, xl, yl):
    dMin =  (abs(row-(xl[0]-1))+ abs(col-(yl[0]-1)))
    for i in range(1, len(xl)):
        dMin =  min(dMin, (abs(row-(xl[i]-1))+ abs(col-(yl[i]-1))))

    return dMin



# Complete the function below.

def  getLockerDistanceGrid( cityLength,  cityWidth,  lockerXCoordinates,  lockerYCoordinates):
    # generate an array of zeros size of the city
    cityPoints =  [[0 for i in range(cityLength)] for k in range(cityWidth)]

    # iterate through city points
    for row in range(cityLength):
        for col in range(cityWidth):
            cityPoints[col][row] = getMinDist(row, col, lockerXCoordinates, lockerYCoordinates)

    for i in range(cityWidth):
        print "".join(map(str,cityPoints[i]))






def main():
    cityLen = int(raw_input().strip())
    cityWid = int(raw_input().strip())
    locX = input()
    locY = input()
    getMinDist(0,0, locX, locY)
    getLockerDistanceGrid( cityLen,  cityWid,  locX,  locY)




if __name__ == '__main__':
    main()
