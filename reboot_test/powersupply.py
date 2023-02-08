
import serial


class powersupply:
    def __init__(self, tty):
        print(f"Using {tty} for keysight")

    def __enter__(self):
        self.PowerOn()
        print("enter powersupply")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.OutDisable()
        self.PowerOff()
        print("exit powersupply")

    
    def PowerOn(self):
        print("powersupply on")

    def PowerOff(self):
        print("powersupply off")


    def OutEnable(self):
        print("Output enable")

    def OutDisable(self):
        print("Output disable")
