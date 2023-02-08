
import serial


class powersupply:
    def __init__(self):
        pass

    def __enter__(self):
        self.PowerOn()
        print("enter powersupply")
        pass
    def __exit__(self):
        self.OutDisable()
        self.PowerOff()
        print("exit powersupply")
        pass
    
    def PowerOn(self):
        print("powersupply on")
        pass
    def PowerOff(self):
        print("powersupply off")
        pass

    def OutEnable(self):
        print("Output enable")
        pass
    def OutDisable(self):
        print("Output disable")
        pass