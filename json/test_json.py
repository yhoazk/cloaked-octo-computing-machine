#!/usr/bin/env python3

import json
import sys
"""
Using the json library
"""

def main(json_path):
    parsed_json = json.load(open(json_path, "r"))
    print("Json load returns an object of type: " + str(type(parsed_json)))
    print("The first elements in the hierarchy are: ")
    [print(e) for e in parsed_json]




if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(sys.argv[0] + "Needs a path to a json as only parameter to work")
    else:
        main(sys.argv[1])
