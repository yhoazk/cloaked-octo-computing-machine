#!/usr/bin/python
"""
Python perform an action for a certain amount of time
"""
import time

def get_lapse(s):
    """
    This function returns a close wich will return true while the time
    period is still valid
    """
    stop = int(time.time() + s)
    def do_for_seconds():
        return int(time.time()) < stop
    return do_for_seconds

def print_stuff():
    print("ss")

def main():
    lap = get_lapse(5)
    while(lap()):
        print "."

if __name__ == "__main__":
    main()
