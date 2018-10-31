#!/usr/bin/env python

import re
"""
Demo for the use case when we want to get the key with the max value in a
dictionary
"""

values = {"a": 20, "b":25, "c":40, "d":50}

print(values[max(values, key=values.get)])


"""
Given a dict of dicts get all the elements that have
certain proprety
"""

req_table = {
    "REQ_4001" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 1},
    "REQ_0051" : {"R_STAT":True, "V_STAT":True, "TYPE":"X", "LINE": 23},
    "REQ_0741" : {"R_STAT":True, "V_STAT":False, "TYPE":"Y", "LINE": 32},
    "REQ_0701" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 2353},
    "REQ_0061" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 341},
    "REQ_0081" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 2345},
    "REQ_0001" : {"R_STAT":True, "V_STAT":True, "TYPE":"Y", "LINE": 23467},
    "REQ_0501" : {"R_STAT":False, "V_STAT":False, "TYPE":"X", "LINE": 2328},
    "REQ_7061" : {"R_STAT":True, "V_STAT":False, "TYPE":"Y", "LINE": 44},
    "REQ_0207" : {"R_STAT":True, "V_STAT":True, "TYPE":"Y", "LINE": 1},
    "REQ_0729" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 3},
    "REQ_0072" : {"R_STAT":False, "V_STAT":True, "TYPE":"X", "LINE": 45},
    "REQ_0084" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 72},
    "REQ_8006" : {"R_STAT":True, "V_STAT":False, "TYPE":"Y", "LINE": 642},
    "REQ_0914" : {"R_STAT":True, "V_STAT":False, "TYPE":"Y", "LINE": 244},
    "REQ_0037" : {"R_STAT":False, "V_STAT":False, "TYPE":"X", "LINE": 252},
    "REQ_0407" : {"R_STAT":True, "V_STAT":False, "TYPE":"X", "LINE": 22222},
    "REQ_0705" : {"R_STAT":True, "V_STAT":False, "TYPE":"Y", "LINE": 2345464},
}


def count_prop(prop, with_val, rq_table, invert=False):
    return len(list(filter(lambda tc : (tc[1][prop] == with_val)^invert, rq_table.items())))

print("Number of tst: {}".format(len(req_table)))
print("Rstat passing: {}".format(count_prop('R_STAT', True, req_table)))
print("Rstat Failing: {}".format(count_prop('R_STAT', False, req_table)))
print("Vstat passing: {}".format(count_prop('V_STAT', True, req_table)))
print("Vstat failing: {}".format(count_prop('V_STAT', False, req_table)))


print("Nr of test X: {}".format(count_prop('TYPE', 'X', req_table)))
print("Nr of test Y: {}".format(count_prop('TYPE', 'Y', req_table)))



def parse_md(file="table_a.md"):
    #is_table_sep = re.compile(r"^(\|\s?:?-+:?\s?)+\|$") # ^((\|\s?:?-+:?\s?)+\|?)$
    #is_table_sep = re.compile(r"^((\|\s?:?-+:?\s?)+\|?)$")
    is_table_sep = re.compile(r"(\|\s?:?-+:?\s?)")
    title_fields = re.compile(r"(\|\s?[A-Za-z0-9\s]*)")
    with open(file, 'r') as table_file:
        past_line = ""
        for line in table_file:
            table_match = is_table_sep.match(line)
            if table_match is not None:
                print("Table width: {}".format(len(table_match.groups())))
                print("last line")
                print(past_line)
                
                print([m.replace(" ", "") for m in title_fields.findall(past_line) ])

            past_line = line

print(20*"-" + "Parse Line" + 20*"-")
parse_md()