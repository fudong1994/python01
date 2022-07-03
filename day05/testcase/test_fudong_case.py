"""
# @Time : 2022/5/23 0023   19:22
# @File : test_login_case
# @Project : python01
# @Content :
"""

import unittest
from day05.login_func import login_check

"""
unittest中的测试用例编写规范
1、定义一个测试用例类，必须继承unittest模块中的TestCase
2、测试用例类中，一个test开头的方法就是一条用例
3、将测试用例执行的代码逻辑写到对应的测试方法中
    #第一步：准备用例数据
    #第二步：调用被测的功能函数(发送请求调用接口)，获取实际结果
    #第三部：断言
"""


class TestLoginFudong(unittest.TestCase):

    def test_login_pass(self):
        # 第一步：准备用例数据
        params = {"username": "python35", "password": "lemonban"}
        expected = {"code": 0, "msg": "登录成功"}
        # 第二步：调用被测的功能函数(发送请求调用接口)，获取实际结果
        result = login_check(**params)
        # 第三部：断言
        assert expected == result

    def test_login_pwd_error(self):
        # 第一步：准备用例数据
        params = {"username": "python35", "password": "lemonban11"}
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：调用被测的功能函数(发送请求调用接口)，获取实际结果
        result = login_check(**params)
        # 第三部：断言
        assert expected == result

    def test_login_user_error(self):
        # 第一步：准备用例数据
        params = {"username": "python66", "password": "lemonban"}
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：调用被测的功能函数(发送请求调用接口)，获取实际结果
        result = login_check(**params)
        # 第三部：断言
        assert expected == result


class TestRegisterFudong(unittest.TestCase):

    def test_register_01(self):
        assert "OK" == "NO"

    def test_register_02(self):
        assert "100" == "100"
