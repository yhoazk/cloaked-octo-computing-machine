#!/usr/bin/env python
#http://preshing.com/20110920/the-python-with-statement-by-example/
class ctx_mgr():
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print("Entering: " + self.name)
    def __exit__(self, type, val, trcbk):
        print("Exiting ctx:" + self.name)

with ctx_mgr("test") as ctx:
    pass