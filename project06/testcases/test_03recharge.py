"""
充值的前提：登录-->提前token
unittest：
    用例级别的前置：setup
    测试类级别的前置：setupclass

"""
import unittest
import requests
from jsonpath import jsonpath
import os
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handler_log import my_log
from common.handle_mysql import HandleDB
from common.tools import replace_data


@ddt
class TestRecharge(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apicases.xlsx"), "recharge")
    cases = excel.read_data()
    db = HandleDB()

    @classmethod
    def setUpClass(cls):
        """用例类的前置方法，登录获取token"""
        # 1、请求登录接口、进行登录
        url = conf.get("env", "base_url") + "/member/login"
        params = {
            "mobile_phone": conf.get("test_data", "mobile"),
            "pwd": conf.get("test_data", "pwd")
        }
        headers = eval(conf.get("env", "headers"))
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # print(res)

        # 2、登录成功之后提前token
        token = jsonpath(res, '$..token')[0]
        # 将token放到请求头
        headers["Authorization"] = "Bearer " + token
        # 保存含有token的请求头为类属性
        cls.headers = headers
        # setattr(TestRecharge, 'headers', headers)

        # 3、提取用户id给充值接口使用
        cls.member_id = jsonpath(res, '$..id')[0]

    @list_data(cases)
    def test_rechaerge(self, item):
        # 1、准备数据
        url = conf.get("env", "base_url") + item['url']
        # ********************************动态替换参数******************************************************
        # 动态处理需要替换的参数
        # item['data'] = item['data'].replace('#member_id#', str(self.member_id))
        item['data'] = replace_data(item['data'], TestRecharge)

        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()
        row = item['case_id'] + 1

        # &&&&&&&&&&&&&&&&&&&&&&&&请求之前查询余额&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        sql = "select leave_amount from futureloan.member where mobile_phone = '{}'".format(
            conf.get("test_data", "mobile"))
        start_amount = self.db.find_one(sql)[0]
        print("用例执行之前，余额为：", start_amount)
        # 2、 发送请求
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果:", res)

        # &&&&&&&&&&&&&&&&&&&&&&&&请求之后查询余额&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        end_amount = self.db.find_one(sql)[0]
        print("用例执行之后，余额为：", end_amount)
        # 3、断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            # &&&&&&&&&&&&&&&&&&&&&&&&校验数据库变化是否等于充值金额&&&&&&&&&&&&&&&&&&&&&&&&&&&&
            if res['msg'] == 'OK':
                self.assertEqual(float(end_amount - start_amount), params['amount'])
            else:
                self.assertEqual(float(end_amount - start_amount), 0)

        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="不通过")
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--【{}】--执行成功".format(item['title']))
            self.excel.write_data(row=row, column=8, value="通过")
