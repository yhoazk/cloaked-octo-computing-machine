import pyvisa



class keysight:
    def __init__(self, tty):
        print(f"Using {tty} for keysight")

    def __enter__(self):
        self.PowerOn()
        print("enter keysight")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.PowerOff()

        print("exit keysight")
    def PowerOn(self):
        print("Keysight power on")

    def PowerOff(self):
        print("Keysight power off")
    def StartMeasurement(self):
        print("start measurement")