#!/usr/bin/env python


import xunitparser

def get_staticstics(path):
    _, tr = xunitparser.parse(path)
    failed = len(tr.failures)
    test = tr.testsRun
    skipped = len(tr.skipped)
    details = ["Test Name: {} \nTest Series: {} \n{}".format(tc.methodname, tc.classname, tc.message) for tc, _ in tr.failures]
    print("\n\n".join(details))
    print("Failed {}  Total Test: {} Skipped {}".format(failed, test, skipped))

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