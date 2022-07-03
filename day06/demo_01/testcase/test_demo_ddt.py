"""
# @Time : 2022/5/23 0023   23:08
# @File : test_demo_ddt
# @Project : python01
# @Content :
"""

"""

ddt的使用步骤：
    1、测试类前面使用@ddt
    2、在测试方法前使用@list_data(测试数据)
    3、在测试方法中定义一个参数，用来接收用例数据
    
"""

import unittest
from unittestreport import ddt, list_data

# -----------案例1---------------
# @ddt
# class TestMusen(unittest.TestCase):
#     @list_data([122, 23, 3, 4, 56])
#     def test_01(self, item):
#         print("item", item)
#         pass

cases = [
    {"title": "666", "expected": "OK", "data": 11},
    {"expected": "OK", "data": 22},
    {"expected": "OK", "data": 33},
    {"expected": "OK", "data": 44}
]


@ddt
class TestMusen(unittest.TestCase):
    @list_data(cases)
    def test_01(self, item):
        print("item", item)
        pass
