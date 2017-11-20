#!/usr/bin/env python

"""
The issue with calling a subprocess is that sometimes the process
is not synchronous, and returns the handler without finishing the
job. (The process is forked, not finished)
"""

import os
import subprocess
import time

"""
Calling a test application written in java
"""
result = subprocess.Popen(["java", "test_app"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
print "Result:" + str(result)
