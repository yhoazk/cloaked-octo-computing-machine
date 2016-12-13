#!/usr/bin/python


x  = [1,2,3,4]

print "initial X values: " + srt(x)
print "Appending [6,7] to x"
x.append([6,7])
print "Appended X values: " + srt(x) 
print  "-------------"
x  = [1,2,3,4]
print "Extend x with [6,7]"
x.extend([6,7])
print "Extended X values: " + srt(x) 

"""
Expected output

initial X values: [1, 2, 3, 4]
Appending [6,7] to x
Appended X values: [1, 2, 3, 4, [6, 7]]
-------------
Extend x with [6,7]
Extended X values: [1, 2, 3, 4, 6, 7]

"""
