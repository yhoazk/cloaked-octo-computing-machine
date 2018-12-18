#!/usr/bin/env python3

"""
This equation is only for the speed, we need to derive
an specialization of this eq to get the x/y trajectory.
"""

import matplotlib.pyplot as plt
import numpy as np

def mjtg(current, setpoint, freq, movetime):
    trajectory = []
    trajectory_derivative = []
    timefreq = int(movetime * freq)

    for time in range(1, timefreq):
        trajectory.append(
            current + (setpoint - current) *
           (10.0 * (time / timefreq) ** 3
            - 15.0 * (time / timefreq) ** 4
            + 6.0 * (time / timefreq) ** 5)
        )

        trajectory_derivative.append(
            freq * (setpoint - current) *
            (30.0 * float((time)**2) * (1.0 / timefreq)**3
            - 60.0 * (time)**3 * (1.0/timefreq)**4
            + 30.0 * time**4 * (1.0 / timefreq)**5)
        )

    return trajectory, trajectory_derivative

avg_vel = 25.0 # 
current = 0.0
setpoint = 180.0
freq = 1000
time = (setpoint - current) / avg_vel

traj, vel = mjtg(current, setpoint, freq, time)

x = [ i/freq for i in range(1, int(time * freq)) ]
plt.plot(x, traj)
plt.plot(x, vel)
plt.title("Min jerk Trajectory")
plt.xlabel("Time [s]")
plt.ylabel("Angle [deg] and angular vel [deg/s]")
plt.legend(["pos", "vel"])
plt.grid(True)
plt.show()