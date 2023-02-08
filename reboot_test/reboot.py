#!/usr/bin/env python3


import pyvisa
import time
from statemachine import StateMachine, State
from keysight  import *
from powersupply import *
from datetime import datetime
import argparse
import signal, os

done = False
def sg(signal, frame):
    global done
    done = True


class RebootCycleTest: 
    # Off = State("Off", initial=True)
    # NormalOp = State("NormalOp")
    # ErrorDetect = State("ErrorDetect")
    # WaitRecover = State("WaitRecover")

    # Cycle = off.to(NormalOp) | NormalOp.to(ErrorDetect) | ErrorDetect.to(Off)


    def __init__(self, ps, key):
        self.powersupply = ps
        self.keysight = key

    def __enter__(self):
        print("Enter reboot cylce")
        ts = datetime.now().strftime("%Y%m%d_%H-%H-%S")
        self.log = open(f"measurement_{ts}.log", "x")
        return self


    def __exit__(self, exc_type, exc_value, exc_tb):
        self.log.close()
        if exc_type is KeyboardInterrupt:
            return True
        return exc_type is None
 

    def pon(self):
        self.log.write("x")
        print("pwer")


def getargs():
    p = argparse.ArgumentParser(usage="reboot.py --tty /dev/ttyUSB0")
    p.add_argument("-tps", "--ttyps")
    p.add_argument("-tks", "--ttykey")
    return vars(p.parse_args())

def main():
    global done
    args = getargs()
    if args["ttyps"]:
        print(f"Terminal to use {args['ttyps']}")
        with powersupply(args["ttyps"]) as ps, keysight(args["ttykey"]) as  ks:
            with RebootCycleTest(ps, ks) as rebooter:
                while done == False:
                    time.sleep(1)
                    rebooter.pon()
                else:
                    print("terminate")


    else:
        print("no tty in args")

if __name__ == "__main__":
    signal.signal(signalnum=signal.SIGINT, handler=sg)
    main()