"""
# @Time : 2022/5/23 0023   21:08
# @File : test_demo3
# @Project : python01
# @Content :
"""
import unittest

"""
fixtrue:测试夹具

1、用例级别：
setup:用例级别的前置，每条用例执行之前都会执行执行
tearDown：用例级别的前置，每条用例执行之后都会执行执行
    
2、测试类级别：
setUpClass：测试类级别的前置：测试类中的用例执行前执行
tearDownClass：测试类级别的后置：所有测试用例执行完之后执行
   
"""


class TestMusen(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 测试类级别的前置
        print("------setUpClass-----")

    @classmethod
    def tearDownClass(cls) -> None:
        # 测试类级别的后置
        print("------tearDownClass-----")

    # 每条用例执行之前都会执行，用例前置脚本
    def setUp(self) -> None:
        print("这个---setUp---方法")

    def tearDown(self) -> None:
        print("这个---tearDown---方法")

    def test_01(self):
        print("这是第1条测试用例")

    def test_02(self):
        print("这是第2条测试用例")

    def test_03(self):
        print("这是第3条测试用例")

    def test_04(self):
        print("这是第4条测试用例")
