"""
# @Time : 2022/5/23 0023   19:53
# @File : run
# @Project : python01
# @Content :
"""
import unittest
from unittestreport import TestRunner

sutie = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\day05\testcase')

runner = TestRunner(sutie)
runner.run()
