import numpy as np
import matplotlib.pyplot as plt
import random
from collections import deque

class quick_lpf:
    def __init__(self, nT1=3, nT2=10):
        """
        Create an averaging filter with 2 stages
        """
        # Queue size
        self.nTaps1 = nT1
        self.nTaps2 = nT2
        # Limit factors
        self.limitFactor1 = 0.35
        self.limitFactor2 = 1 - self.limitFactor1
        # Create the queues to contain the data
        self.queue1 = deque(maxlen=self.nTaps1)
        self.queue2 = deque(maxlen=self.nTaps2)

    def filter(self, new_val):



def test_filter():
    N = 50
    step = np.concatenate((np.zeros(N),np.ones(N)))
    ramp = np.concatenate((np.zeros(N/2),np.linspace(0,100,N/2), np.linspace(100,0,N/2), np.zeros(N/2)))



if "__main__" = __name__:


