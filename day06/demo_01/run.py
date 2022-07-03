"""
# @Time : 2022/5/24 0024   14:12
# @File : run
# @Project : python01
# @Content :
"""

from unittestreport import TestRunner
import unittest

sutie = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\day06\demo_01\testcase')

runner = TestRunner(sutie)

runner.run()
