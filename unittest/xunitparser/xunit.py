#!/usr/bin/env python


import xunitparser

def get_staticstics(path):
    ts, tr = xunitparser.parse(path)
    #print(dir(tr))
    failed = len(tr.failures)
    test = tr.testsRun
    skipped = len(tr.skipped)
    details = ["Test Name: {} \n {}".format(tc[0].methodname, tc[0].message) for tc in tr.failures]
    #print(len(tr.failures))
    #a,b = tr.failures[0]
    #print("-"*40 + "\n" + a.message)
    #print("Method name: " + a.methodname)
    #print(b)
    print("\n\n".join(details))
    print("Failed {}  Total Test: {} Skipped {}".format(failed, test, skipped))
get_staticstics("../samples/gtest_with_failure.xml")