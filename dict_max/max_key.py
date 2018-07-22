#!/usr/bin/env python

"""
Demo for the use case when we want to get the key with the max value in a
dictionary
"""

values = {"a": 20, "b":25, "c":40, "d":50}

print(values[max(values, key=values.get)])
