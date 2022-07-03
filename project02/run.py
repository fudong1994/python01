"""
# @Time : 2022/6/5 0005   23:35
# @File : run
# @Project : project01
# @Content :
"""

import unittest
from unittestreport import TestRunner
from common.handle_path import CASES_DIR, REPORT_DIR

suite = unittest.defaultTestLoader.discover(CASES_DIR)

runner = TestRunner(suite, filename="py666.html",
                    report_dir=REPORT_DIR, )

runner.run()
