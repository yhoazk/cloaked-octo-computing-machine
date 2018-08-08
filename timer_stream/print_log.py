#!/usr/bin/env python

from time import sleep, time
import signal, os

start = None
stop = None
def timer_stop():
    stop = time() - start
    print("Seconds:" + str(stop))



log = open("log.log", "r")

for l in log:
    print(l, end="")
    sleep(.3)
