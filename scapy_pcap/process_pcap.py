#!/usr/bin/env python3

import argparse
import os
import sys
from scapy.utils import RawPcapReader
import time

def printable_timestamp(ts, resol):
    ts_sec = ts // resol
    ts_subsec = ts % resol
    ts_sec_str = time.strftime("%Y-%m-%d %H:%M%S", time.localtime(ts_sec))
    return "{}.{}".format(ts_sec_str, ts_subsec)

def interesting_time(file_name):
    from scapy.utils import RawPcapReader
    from scapy.layers.l2 import Ether
    from scapy.layers.inet import IP, TCP

    client = "192.168.1.137:57080"
    server = "152.19.134.43:80"

    (client_ip, client_port) = client.split(':')
    (server_ip, server_port) = server.split(':')
    count = 0
    interesting_packet_count = 0

    for(pkt_data, pkt_metadata, ) in RawPcapReader(file_name):
        count += 1
        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields or ether_pkt.type != 0x0800:
            continue
        
        ip_pkt = ether_pkt[IP]
        not_interesting = (ip_pkt.proto != 6) or \
                 ((ip_pkt.src != server_ip) and (ip_pkt.src != client_ip)) or \
                    ((ip_pkt.dst != server_ip) and (ip_pkt.dst != client_ip))

        if not_interesting:
            continue
        tcp_pkt = ip_pkt[TCP]
        not_interesting = (tcp_pkt.sport != int(server_port)) and \
                            (tcp_pkt.sport != int(client_port)) or \
                          (tcp_pkt.dport != int(server_port)) and \
                            (tcp_pkt.dport != int(client_port))

        if not_interesting:
            continue

        interesting_packet_count += 1
        if interesting_packet_count == 1:
            first_pkt_timestamp = (pkt_metadata.tshigh << 32) | pkt_metadata.tslow
            first_pkt_timestamp_resolution = pkt_metadata.tsresol
            first_pkt_ordinal = count
        
        last_pkt_timestamp = (pkt_metadata.tshigh << 32)  | pkt_metadata.tslow
        last_pkt_timestamp_resolution = pkt_metadata.tsresol
        last_pkt_ordinal = count
    
    print("{} contains {} packets and {} interesting".format(file_name, count, interesting_packet_count))

    print("First packet in connection: #{} {}".format(
        first_pkt_ordinal,
        printable_timestamp(first_pkt_timestamp, first_pkt_timestamp_resolution)
    ))
    print("Last packet in connection: #{} {}".format(
        last_pkt_ordinal,
        printable_timestamp(last_pkt_timestamp, last_pkt_timestamp_resolution)
    ))

def interesting_connections(file_name):
    from scapy.utils import RawPcapReader
    from scapy.layers.l2 import Ether
    from scapy.layers.inet import IP, TCP

    client = "192.168.1.137:57080"
    server = "152.19.134.43:80"

    (client_ip, client_port) = client.split(':')
    (server_ip, server_port) = server.split(':')
    count = 0
    interesting_packet_count = 0

    for(pkt_data, pkt_metadata, ) in RawPcapReader(file_name):
        count += 1
        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields or ether_pkt.type != 0x0800:
            continue
        
        ip_pkt = ether_pkt[IP]
        not_interesting = (ip_pkt.proto != 6) or \
                 ((ip_pkt.src != server_ip) and (ip_pkt.src != client_ip)) or \
                    ((ip_pkt.dst != server_ip) and (ip_pkt.dst != client_ip))

        if not_interesting:
            continue
        tcp_pkt = ip_pkt[TCP]
        not_interesting = (tcp_pkt.sport != int(server_port)) and \
                            (tcp_pkt.sport != int(client_port)) or \
                          (tcp_pkt.dport != int(server_port)) and \
                            (tcp_pkt.dport != int(client_port))

        if not_interesting:
            continue

        interesting_packet_count += 1
    
    print("{} contains {} packets and {} interesting".format(file_name, count, interesting_packet_count))

        
            

def filter_pcap(file_name):
    from scapy.utils import RawPcapReader
    from scapy.layers.l2 import Ether
    from scapy.layers.inet import IP, TCP

    count = 0
    interesting_packet_count = 0

    for (pkt_data, pkt_metadata, ) in RawPcapReader(file_name):
        count += 1
        ether_pkt = Ether(pkt_data)
        if 'type' not in ether_pkt.fields:
            # LLC frames will have len instead of type
            continue

        if ether_pkt.type != 0x0800:
            # Not an IPv4 pkt
            continue

        ip_pkt = ether_pkt[IP]
        if ip_pkt.proto != 6:
            # ifnore non-TCP packet
            continue
        
        interesting_packet_count += 1

    print("{} contains {} packets {} interesting".format(file_name, count, interesting_packet_count))

def count_pkgs(file_name):
    count = 0
    for (pkt_data, pkt_metadata,) in RawPcapReader(file_name):
        count += 1
    
    print("{} contains {} packets".format(file_name, count))
def process_pcap(file_name):
    print("Opening {}".format(file_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PCAP reader")
    parser.add_argument("--pcap", metavar="<pcap file name>",
                        help="pcap file to parse", required=True)
    args = parser.parse_args()

    file_name = args.pcap

    if not os.path.isfile(file_name):
        print("{} does not exists.".format(file_name), file=sys.stderr)
        sys.exit(1)
    
    interesting_time(file_name)
    sys.exit(0)