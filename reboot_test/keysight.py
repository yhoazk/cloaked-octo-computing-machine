import pyvisa



class keysight:
    def __init__(self):
        pass

    def __enter__(self):
        self.PowerOn()
        print("enter keysight")
        pass
    def __exit__(self):
        self.PowerOff()
        
        print("exit keysight")
        pass
    def PowerOn(self):
        print("Keysight power on")
        pass

    def PowerOff(self):
        print("Keysight power off")
        pass
    def StartMeasurement(self):
        print("start measurement")