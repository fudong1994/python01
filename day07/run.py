"""
# @Time : 2022/5/24 0024   16:34
# @File : run
# @Project : python01
# @Content :
"""

import unittest
import unittestreport

sutie = unittest.defaultTestLoader.discover(r'D:\pythonworkspace\python01\day07\testcase')

runner = unittestreport.TestRunner(sutie)
runner.run()
