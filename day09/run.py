"""
# @Time : 2022/5/30 0030   10:32
# @File : run
# @Project : python01
# @Content :
"""
import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\day09\testcases')

runner = TestRunner(suite)

runner.run()
