"""
# @Time : 2022/6/5 0005   23:35
# @File : run
# @Project : project01
# @Content :
"""

import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\project01\testcases')

runner = TestRunner(suite, filename="py666.html",
                    report_dir="./reports", )

runner.run()
