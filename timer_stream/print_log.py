#!/usr/bin/env python

from time import sleep, time
import signal, os
import serial


start = None
stop = None
def timer_stop(signum, frame):
    stop = time() - start
    print("Seconds:" + str(stop))



"""
log = open("log.log", "r")

for l in log:
    print(l, end="")
    sleep(.3)
"""
start = time()
signal.signal(signal.SIGUSR2, timer_stop)
sleep(30)
"""
with serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Leonardo-if00', 9600, timeout=1) as ser:
    x = ser.read()          # read one byte
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line
    print(line)
"""

# ./print_log.py &
# kill -SIGUSR2 $!

#sudo cat /dev/serial/by-id/usb-Arduino_LLC_Arduino_Leonardo-if00 | grep -m 1 bin
