"""
# @Time : 2022/5/23 0023   22:48
# @File : test)login
# @Project : python01
# @Content :
"""
import unittest
from unittestreport import ddt, list_data
import openpyxl
from day07.login_func import login_check

workbook = openpyxl.load_workbook('D:\pythonworkspace\python01\day07\cases.xlsx')
sh = workbook["login"]
res = list(sh.rows)
# 获取第一行的表头
title = [i.value for i in res[0]]

cases = []
# 遍历第一行以外的其他行
for item in res[1:]:
    data = [i.value for i in item]
    dic = dict(zip(title, data))
    cases.append(dic)

@ddt
class TestLogin(unittest.TestCase):

    @list_data(cases)
    def test_login(self, item):
        # 第一步：准备数据
        expected = eval(item["expected"])
        params = eval(item["data"])
        # 第二步：调用功能函数，获取实际结果
        res = login_check(**params)
        # 第三步：断言
        self.assertEqual(expected, res)
