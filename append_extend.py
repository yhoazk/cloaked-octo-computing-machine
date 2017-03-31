#!/usr/bin/python


x  = [1,2,3,4]

print "initial X values: " + str(x)
print "Appending [6,7] to x"
x.append([6,7])
print "Appended X values: " + str(x) 
print  "-------------"
x  = [1,2,3,4]
print "Extend x with [6,7]"
x.extend([6,7])
print "Extended X values: " + str(x) 

