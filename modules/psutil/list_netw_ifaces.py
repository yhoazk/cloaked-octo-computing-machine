#!/usr/bin/env python

from __future__ import print_function
import psutil

[print(iface_name) for iface_name in psutil.net_if_addrs().keys()]
