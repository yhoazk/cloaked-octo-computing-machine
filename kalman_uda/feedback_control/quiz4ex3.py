#!/usr/bin/env python3

from matplotlib import pyplot as plt



def sim_system():
    xsol = []
    xdot = []
    xdas = []
    y = []
    x1,x2,x3 = 1,1,1
    x1_,x2_,x3_ = 0,0,0

    k1,k2,k3 = 1, 3, 5
    y = [n*0.01 for n in range(100)]
    for _ in y:
        #y.append(n)
        x1_ = 2*x1  -k1*x1
        x2_ = 2*x2  -k2*x2
        x3_ = 2*x3  -k3*x3
        print(" {} {} {}".format(x1_, x2_, x3_))
        xsol.append(x1_)
        xdot.append(x2_)
        xdas.append(x3_)
        x1,x2,x3 = x1_,x2_,x3_

    plt.plot(xsol, y, '-')
    plt.plot(xdas, y, '*')
    plt.plot(xdot, y, 'o')
    plt.show()

if __name__ == "__main__":
    sim_system()