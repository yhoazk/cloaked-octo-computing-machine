#!/usr/bin/env python



"""Check for input every 0.1 seconds. Treat available input
immediately, but do something else if idle.

This snipped can be used for readnig the TTY/STDOUT/STDIN without
blocking the program.
https://repolinux.wordpress.com/2012/10/09/non-blocking-read-from-stdin-in-python/

An option is to use the library signal and schedule a alarm for a timeout,

Yet another option is a queue and a subprocess.
"""

import sys
import select
import time

# files monitored for input
read_list = [sys.stdin]
# select() should wait for this many seconds for input.
# A smaller number means more cpu usage, but a greater one
# means a more noticeable delay between input becoming
# available and the program starting to work on it.
timeout = 0.1 # seconds
last_work_time = time.time()

def treat_input(linein):
  global last_work_time
  print("Workin' it!" + linein)
  time.sleep(1) # working takes time
  print('Done')
  last_work_time = time.time()

def idle_work():
  global last_work_time
  now = time.time()
  # do some other stuff every 2 seconds of idleness
  if now - last_work_time > 2:
    print('Idle for too long; doing some other stuff.')
    last_work_time = now

def main_loop():
  global read_list
  # while still waiting for input on at least one file
  while read_list:
    ready = select.select(read_list, [], [], timeout)[0]
    if not ready:
      idle_work()
    else:
      for file in ready:
        line = file.readline()
        if not line: # EOF, remove file from input list
          read_list.remove(file)
        elif line.rstrip(): # optional: skipping empty lines
          treat_input(line)

try:
    main_loop()
except KeyboardInterrupt:
  pass
