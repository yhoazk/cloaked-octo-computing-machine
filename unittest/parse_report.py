#!/usr/bin/env python

from junitparser import JUnitXml

result = JUnitXml.fromfile("./sample2.xml")

result.update_statistics()
print("Result errors {}".format(result.errors))
print("Result tests {}".format(result.tests))
"""
Check that the tags are correctly in the xml
The system-out and system-error should be inside the testcase
"""

for suite in result:
    print("Test suite name: {}".format(suite.name))
    #print(dir(suite))
    print("-"*90)
    for case in suite:
        print(dir(case))
        print("tests case name "  + case.name)
        print(case.result)
        print(case.system_out)
        print(case.system_err)