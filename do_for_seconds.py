
"""
Python perform an action for a certain amount of time
"""

from datetime import datetime

def do_for_seconds(n, action):
    _now = datetime.now()
    stop = _now.second + n
    while(datetime.now().second < stop):
        print("Second:" + str(datetime.now().second))
        action()

def print_stuff():
    print("ss")

def main():
    do_for_seconds(5, print_stuff)

if __name__ == "__main__":
    main()
