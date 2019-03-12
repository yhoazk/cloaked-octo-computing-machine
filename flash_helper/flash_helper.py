#!/usr/env python3

import subprocess
import sys
import os

class dialog:
  def __init__(self):
    print("dialog created")

  def msg(self, msg):
    subprocess.call(["touch", "/tmp/reee"])
    

if __name__ == "__main__":
  dg = dialog()
  dg.msg("dssd")