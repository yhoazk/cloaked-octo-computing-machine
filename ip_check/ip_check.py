#!/usr/bin/env python3

import json
import subprocess
import os


"""
sudo brctl addbr eth0.73
sudo brctl addbr external_br
sudo brctl addif external_br enp7s0
"""

def is_mac(dct):
    d = {}
    for prop, val in dct:
        if "address" == prop: # ignore MAC mismatch
            d["address"] = "xx:xx:xx:xx:xx:xx"
        if "local" == prop and (':' in val): # ignore IPv6 addresses
            d["local"] = "::x"
        else:
            d[prop] = val
    return d

def current_config():
    proc = subprocess.Popen(["ip", "-j", "a"], stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    cfg = json.loads(out, object_pairs_hook=is_mac)
    return cfg

def compare_memeber(json_element):
    pass

def sort_by_iface(json_list):
    return sorted(json_list, key=lambda iface_descr: iface_descr["ifname"] )



if __name__ == "__main__":
    with open("golden_config.json") as cfg_fd:
        golden_cfg = sort_by_iface(json.load(cfg_fd, object_pairs_hook=is_mac))
        current_cfg = sort_by_iface(current_config())
        if golden_cfg == current_cfg:
            print("AOK")
        else:
            print("NNNOK")
        for propa, propb in zip(golden_cfg, current_cfg):
            print(propa)
            for (iface_a_k, iface_a_v), (iface_b_k, iface_b_v) in zip(propa.items(), propb.items()):
                #print(f"Comparing {iface_a['ifname']} with {iface_b['ifname']}")
                sm = iface_a_v ==iface_b_v
                print("-"*30)
                print(f"{iface_a_k} == {iface_b_k} vals {iface_a_v} {iface_b_v}  ? {sm}" )
                print("-"*30)