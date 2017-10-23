#!/usr/bin/env python
"""
Given an actual point and the target point
calculate the speeds such as the speed at the
target point is 0.
This minimizing the jerk
"""
import numpy as np
from numpy.core.multiarray import interp as np_interp
import matplotlib.pyplot as plt

initial_point = 250
final_point   = 400

initial_speed  = 70


initial_buffer = np.ones(20) # store the last speeds
def get_speeds(init_indx, final_indx, current_speed):
    indx = range(init_indx, final_indx)
    speeds = np_interp(indx, initial_buffer, )
    return ()



def main():
    points, speeds = get_speeds(initial_point, final_point, initial_speed)
    plt.plot(points, speeds)
    plt.show()

if __name__ == "__main__":
    # for this test, the initial speed is 56
    initial_buffer = initial_buffer * initial_speed
    main()
