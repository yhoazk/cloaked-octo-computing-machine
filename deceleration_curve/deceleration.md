#!/usr/bin/env python


"""
Snippet to create a deceleration target velocities for nanodegree.
The input is current velocity
    - The speed of the vehicle we want to stop
current pose
    - The position of the vehicle
final pose
    - The position where the vehicle has to have the target velocity

The purpose is to create an algorithm such as the generated velocities
do not exceed a jerk > 10 m/s^3

Steps:
    * keep a buffer of the 10 past velocities
    * with the information given in the buffer calculate a spline
      which ends at the desited position and the desired speed (0)
https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.interp.html
"""

import numpy as np
from numpy.core.multiarray import interp as compiled_interp




def main():
    pass



if __name__ == "__main__":
    main()
