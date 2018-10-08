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
    details = ["Test Name: {} \nTest Series: {} \n{}".format(tc.methodname, tc.classname, tc.message) for tc, _ in tr.failures]
    print("\n\n".join(details))

    xml  = ElementTree.parse(path).getroot()
    disabled = 0
    if xml.tag == 'testsuites' and 'disabled' in xml.attrib:
        disabled = int(xml.attrib['disabled'])
    else:
        # disabled not in testsuites, collect the disabled tests in testsuite
        disabled = sum(int(ts.attrib['disabled']) for ts in xml if ts.tag == 'testsuite' and 'disabled' in ts.attrib)
    print("Failed {}  Total Test: {} Skipped {} Disabled {}".format(failed, test, skipped, disabled))

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