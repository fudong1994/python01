"""
# @Time : 2022/5/23 0023   22:48
# @File : test)login
# @Project : python01
# @Content :
"""

import unittest
from day06.demo_01.login_func import login_check
from unittestreport import ddt, list_data

"""
ddt的使用步骤：
    1、测试类前面使用@ddt
    2、在测试方法前使用@list_data(测试数据)
    3、在测试方法中定义一个参数，用来接收用例数据
    
如果需要给用例添加描述：需求在测试数据中添加一个title字段（测试数据需要是字字典类型）
"""

cases = [
    {"title": "登录成功", "expected": {"code": 0, "msg": "登录成功"},
     "params": {"username": "python35", "password": "lemonban"}},
    {"title": "登录成功02", "expected": {"code": 0, "msg": "登录成功"},
     "params": {"username": "python35", "password": "lemonban"}}
]


@ddt
class TestLogin(unittest.TestCase):

    @list_data(cases)
    def test_login(self, item):
        # 准备用例数据
        data = item["params"]
        expected = item["expected"]
        # 调用被测函数，获取实际的结果
        res = login_check(**data)
        # 断言
        self.assertEqual(expected, res)
