"""
# @Time : 2022/5/23 0023   21:08
# @File : test_demo3
# @Project : python01
# @Content :
"""
import unittest

"""
unittest提供的断言
   
"""


class TestMusen(unittest.TestCase):

    def test_01(self):
        print("这是第1条测试用例")
        # 断言相等
        # assert 200 == 201
        # self.assertEqual(200, 201)

        # 成员断言
        # data = ["11", "22"]
        # n = "11"
        # assert n in data
        # self.assertIn(n, data)
        self.assertIn("错误", "您输入的账号密码错误")
