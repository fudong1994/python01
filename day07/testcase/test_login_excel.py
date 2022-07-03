"""
# @Time : 2022/5/23 0023   22:48
# @File : test)login
# @Project : python01
# @Content :
"""
import unittest
from unittestreport import ddt, list_data
from day07.login_func import login_check
from day07.demo.handle_excel import HandleExcel


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel("D:\pythonworkspace\python01\day07\cases.xlsx", "login")
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self, item):
        # 第一步：准备数据
        expected = eval(item["expected"])
        params = eval(item["data"])
        row = item["case_id"] + 1
        # 第二步：调用功能函数，获取实际结果
        res = login_check(**params)
        # 第三步：断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print("测试用例执行未通过")
            self.excel.write_data(row=row, column=5, value="未通过")
            # 为了让unittest识别这条是未通过的用例，捕获异常处理后要主动把异常跑出去
            raise e
        else:
            print("用例执行通过")
            self.excel.write_data(row=row, column=5, value="通过")
