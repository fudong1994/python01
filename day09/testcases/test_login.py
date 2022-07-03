"""
# @Time : 2022/5/30 0030   10:11
# @File : test_login
# @Project : python01
# @Content :
"""

import unittest
from unittestreport import ddt, list_data
from day09.handle_excel import HandleExcel
from day09.login_func import login_check
from day09.handler_log import my_log


# 创建一个日志收集器
# my_log = create_log()


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel('D:\pythonworkspace\python01\day09\cases.xlsx', 'login')
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self, item):
        # 1、准备用例数据
        expected = eval(item['expected'])
        params = eval(item['data'])
        row = item['case_id'] + 1
        # 2、调用功能函数进行测试，获取结果
        res = login_check(**params)
        # 3、断言-->测试结果回写
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=5, value="不通过")
            my_log.error("用例【{}】---执行失败".format(item['title']))
            # my_log.error(e)
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=5, value="通过")
            my_log.info("用例【{}】---执行成功".format(item['title']))
