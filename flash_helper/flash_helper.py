#!/usr/env python3

import subprocess
import sys
import os
import pyudev
import syslog
from datetime import timedelta
from datetime import datetime
import pickle

cfg_file_name = 'usb_flash_data'

def get_usb_dev():
  ctx = pyudev.Context()
  return ctx.list_devices(subsystem='block', DEVTYPE='partition')

def get_mount_path(node):
  find_cmd = '/{}/{{ print  $2 }}'.format(node.replace('/', '\/'))
  path = subprocess.check_output(['awk', find_cmd, '/proc/mounts'])
  return path.decode().strip()


def save_device_data(data):
  cfg = os.environ['HOME'] + '/.' + cfg_file_name
  with open(cfg, 'wb') as flash_cfg:
    pickle.dump(data, flash_cfg)


def load_dev_data():
  cfg = os.environ['HOME'] + '/.' + cfg_file_name
  with open(cfg, 'rb') as flash_cfg:
    return pickle.load(flash_cfg)

def get_usb_data(dev):
  attrs = ['idProduct', 'idVendor', 'manufacturer', 'serial', 'product']
  def __get_attr(d, attr):
    try:
      return d.attributes.get(attr).decode()
    except:
      return None

  if dev.parent is None:
    return None
  elif dev.driver == 'usb' and dev.subsystem == 'usb':
    __props = {}
    for attr in attrs:
      __props[attr] = __get_attr(dev, attr)
    return __props
  else:
    return get_usb_data(dev.parent)

class dialog:
  zen_default = ['zenity', '--title=Flash_Helper', '--timeout=60']

  def __init__(self):
    print("dialog created")

  def info(self, msg=''):
    info_params=['--info', '--text={}'.format(msg)]
    self.__call_zenity(info_params)

  def __call_zenity(self, params):
    try:
      subprocess.check_output(self.zen_default + params)
    except subprocess.CalledProcessError as e:
      if e.returncode == 1:
        print("Regative Response")
      elif e.returncode == 0:
        print("Positive response")
      elif e.returncode == 5:
        print("timeout")

  def choose(self, l1, l2):
    pass

  def error(self, msg):
    pass


if __name__ == "__main__":
  dg = dialog()
  dg.info("dssd")
  devs = get_usb_dev()
  delta_connection = []
  for d in devs:
    print('{0} :: {1} - {2} Gb'.format(d.device_type, d.device_path, int(d.attributes.get('size').decode('utf-8'))))
    delta_connection.append((d.time_since_initialized, d))

  # The min compares the first member
  time,dev = min(delta_connection)
  print(get_mount_path(dev.device_node))
  dev_data = get_usb_data(dev)
  for k, v in dev_data.items():
    print("{0}:::{1}".format(k, v))
  save_device_data(dev_data)

  data = load_dev_data()
  print("-" * 50)

  for k, v in data.items():
    print("{0}:::{1}".format(k, v))
