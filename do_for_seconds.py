#!/usr/bin/python
"""
Python perform an action for a certain amount of time
"""
import time

def get_lapse(s):
    stop = int(time.time() + s)
    def do_for_seconds():
        while(int(time.time()) < stop):
            print("Second:" + str(int(time.time())) + " Stop: " + str(int(stop)))
            return True
        return False
    return do_for_seconds

def print_stuff():
    print("ss")

def main():
    lap = get_lapse(5)
    while(lap() == True):
        print "."

if __name__ == "__main__":
    main()
