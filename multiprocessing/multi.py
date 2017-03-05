#!/usr/bin/env python

from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == "__main__":
    p = Pool(5)
    print(p.map(f, [2,3,4,5]))
