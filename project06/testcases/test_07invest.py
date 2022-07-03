"""
前置操作：
    1、普通用户登录（类级别）
    2、管理员登录（类级别）
    3、添加项目（类级别）
    4、审核项目（类级别）

"""

import unittest
import os
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handler_log import my_log
from common.tools import replace_data
from testcases.fixture import BaseTest


@ddt
class TestInvest(unittest.TestCase, BaseTest):
    excel = HandleExcel(os.path.join(DATA_DIR, "apicases.xlsx"), "invest")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        # 管理员登录
        cls.admin_login()
        # 普通用户登录
        cls.user_login()
        # 添加项目
        cls.add_project()
        # 审核
        cls.audit()

    @list_data(cases)
    def test_invest(self, item):
        # 第一步：准备用例数据
        url = conf.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestInvest)

        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()
        row = item['case_id'] + 1

        # 第二步：请求接口
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果:", res)

        # 第三步：断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertIn(expected['msg'], res['msg'])
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="不通过")
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--【{}】--执行成功".format(item['title']))
            self.excel.write_data(row=row, column=8, value="通过")
