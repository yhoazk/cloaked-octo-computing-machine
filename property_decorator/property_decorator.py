#!/usr/bin/env python

class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_f(self):
        return (self.get_temperature() * 1.8) + 32
    
    ## needed implementation
    def get_temperature(self):
        print("get the value")
        return self._temperature

    def set_temperature(self, value):
        print(" get the value")
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature) 

class Celsius_decorated:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


t = Celsius(6)
print(t)

