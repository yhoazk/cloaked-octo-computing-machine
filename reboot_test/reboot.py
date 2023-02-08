#!/usr/bin/env python3


import pyvisa
import time
from statemachine import StateMachine, State
import argparse


class RebootCycleTest: 
    # Off = State("Off", initial=True)
    # NormalOp = State("NormalOp")
    # ErrorDetect = State("ErrorDetect")
    # WaitRecover = State("WaitRecover")

    # Cycle = off.to(NormalOp) | NormalOp.to(ErrorDetect) | ErrorDetect.to(Off)


    def __init__(self, ttyps, ttykey):
        self.tty_powersupply = ttyps
        self.tty_keysight = ttykey
    def __enter__(self):
        print("Enter reboot cylce")
        return self
    def __exit__(self):
        print("Exit reboot cycle")
    def pon(self):
        print("pwer")
    
def getargs():
    p = argparse.ArgumentParser(usage="reboot.py --tty /dev/ttyUSB0")
    p.add_argument("-tps", "--ttyps")
    p.add_argument("-tks", "--ttykey")
    return vars(p.parse_args())

def main():
    args = getargs()
    if args["ttyps"]:
        print(f"Terminal to use {args['ttyps']}")
        with RebootCycleTest(args['ttyps'], "/dev/ttyUSB1") as rebooter:
            while True:
                time.sleep(1)
                rebooter.pon()


    else:
        print("no tty in args")

if __name__ == "__main__":
    main()