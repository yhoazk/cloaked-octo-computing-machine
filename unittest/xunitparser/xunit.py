#!/usr/bin/env python


import xunitparser
from xml.etree import ElementTree
'''
How to get the disabled test?
'''

def get_staticstics(path):
    _, tr = xunitparser.parse(path)
    failed = len(tr.failures)
    test = tr.testsRun
    skipped = len(tr.skipped)
    tc_time = 0
    details = ["Test Name: {} \nTest Series: {} \n{}".format(tc.methodname, tc.classname, tc.message) for tc, _ in tr.failures]
    tc_time = sum([tc.time.total_seconds() for tc, _ in tr.failures])
    print("\n\n".join(details))
    print("Failed {}  Total Test: {} Skipped {}".format(failed, test, skipped))
#    print(type(tr.time.total_seconds()))
    if tr.time is not None:
        print("PATH: {}\nTime {} ".format(path, tr.time.total_seconds()))

get_staticstics("../samples/gtest_with_failure.xml")
print(":"*80)
get_staticstics("../samples/sample.xml")
print(":"*80)
get_staticstics("../samples/sample2.xml")
print(":"*80)
get_staticstics("../samples/sample3.xml")
print(":"*80)
get_staticstics("../samples/test.xml")
print(":"*80)
get_staticstics("../samples/report.xml")
print(":"*80)

