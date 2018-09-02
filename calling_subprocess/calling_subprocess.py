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
Calling a test application written in java, and waiting for it to finish
"""
child = subprocess.Popen(["java", "test_app"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = child.communicate()[0]
print("StdOut:" + str(stdout))

"""
Get the retvalue from the executed binary
"""

print("Return code:" + str(child.returncode))
