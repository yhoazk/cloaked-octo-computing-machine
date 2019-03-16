#!/usr/env python3

import subprocess
import sys
import os
import pyudev
import syslog
from datetime import timedelta
from datetime import datetime
def get_usb_dev():
  ctx = pyudev.Context()
  return ctx.list_devices(subsystem='block', DEVTYPE='partition')

def get_mount_path(node):
  find_cmd = '/{}/{{ print  $2 }}'.format(node.replace('/', '\/'))
  path = subprocess.check_output(['awk', find_cmd, '/proc/mounts'])
  print(path)
  return path.decode('utf-8')

def get_usb_data(dev):
  if dev.parent is None:
    return None
  elif dev.driver == 'usb' and dev.subsystem == 'usb':
    print(dev.attributes.get('idProduct'))
    print(dev.attributes.get('manufacturer'))
   # print(list(dev.attributes.available_attributes))
    return (dev.attributes.get('idProduct'), dev.attributes.get('manufacturer'))
  else:
    return get_usb_data(dev.parent)

class dialog:
  def __init__(self):
    print("dialog created")

  def msg(self, msg):
    subprocess.call(["touch", "/tmp/reee"])
    

if __name__ == "__main__":
  #dg = dialog()
  #dg.msg("dssd")
  devs = get_usb_dev()
  for d in devs:
    print(d)
  now = datetime.now()
  delta_connection = []
  for d in devs:
    print('{0} :: {1} - {2} Gb'.format(d.device_type, d.device_path, int(d.attributes.get('size').decode('utf-8'))))
    delta_connection.append((d.time_since_initialized, d))

  # The min compares the first member
  time,dev = min(delta_connection)
  print(time)
  print(dev.device_node)
  get_mount_path(dev.device_node)
  get_usb_data(dev)
