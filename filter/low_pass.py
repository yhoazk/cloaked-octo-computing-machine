import numpy as np
import matplotlib.pyplot as plt
import random
from collections import deque

class quick_lpf:
    def __init__(self, nT1=5, nT2=25):
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
        self.filterGain = 1.1

    def filter(self, new_val):
        # Feed the 1st queue
        self.queue1.append(new_val)
        # feed the 2nd queue
        self.queue2.append(new_val)
        # Add elements and apply averaging
        total_q1 = sum(self.queue1) / float(self.nTaps1)
        total_q2 = sum(self.queue2) / float(self.nTaps2)
        # Apply limiting factor
        ret_val = total_q1 * self.limitFactor1 + total_q2 * self.limitFactor2
        return ret_val * self.filterGain


def test_filter():
    N = 50
    step = np.concatenate((np.zeros(N),np.ones(N)))
    ramp = np.concatenate((np.zeros(N//2),np.linspace(0,100,N//2), np.linspace(100,0,N//2), np.zeros(N//2)))

    lpf_step = quick_lpf(nT1 = 3, nT2=30)
    lpf_ramp = quick_lpf(nT1 = 1, nT2=20)

    filtered_step = []
    filtered_ramp = []

    for stp, rmp in zip(step, ramp):
        filtered_step.append(lpf_step.filter(stp))
        filtered_ramp.append(lpf_ramp.filter(rmp))

    plt.plot(range(len(step)), filtered_step)
    plt.plot(range(len(step)), step)
    plt.show()

    plt.plot(range(len(ramp)), filtered_ramp)
    plt.plot(range(len(ramp)), ramp)
    plt.show()



if "__main__" == __name__:
    test_filter()
