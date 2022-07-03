import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.tools import replace_data
from common.handler_log import my_log
from common.handle_mysql import HandleDB

"""
添加项目：需要登录
    定义用例的前置方法
"""


@ddt
class TestAdd(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'add')
    cases = excel.read_data()
    db = HandleDB()

    @classmethod
    def setUpClass(cls):
        """前置登录"""
        # 1、准备登录的数据
        url = conf.get('env', 'base_url') + "/member/login"
        params = {
            "mobile_phone": conf.get("test_data", "mobile"),
            "pwd": conf.get("test_data", "pwd")
        }
        headers = eval(conf.get("env", "headers"))
        # 2、请求登录接口
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # 3、提取token，放到请求头中
        token = jsonpath(res, '$..token')[0]
        headers["Authorization"] = "Bearer " + token
        cls.headers = headers
        # 4、提取用户id
        cls.member_id = jsonpath(res, '$..id')[0]

    @list_data(cases)
    def test_add(self, item):
        # 第一步：准备数据
        url = conf.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestAdd)

        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()
        row = item['case_id'] + 1

        # 调用接口之前，查询数据库该用户的项目数量
        sql = "select * from futureloan.loan where member_id = {}".format(self.member_id)
        start_count = self.db.find_count(sql)
        print("接口调用之后项目的个数：", start_count)

        # 第二步：调用接口，获取实际结果
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果:", res)

        # 调用接口之后，查询数据库该用户的项目数量
        end_count = self.db.find_count(sql)
        print("接口调用之后项目的个数：", end_count)

        # 第三步：断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            # 判断添加项目是否成功，进行判断是否需求校验数据库
            if res['msg'] == 'OK':
                self.assertEqual(end_count - start_count, 1)
            else:
                self.assertEqual(end_count - start_count, 0)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="不通过")
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--【{}】--执行成功".format(item['title']))
            self.excel.write_data(row=row, column=8, value="通过")
