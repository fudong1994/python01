"""
审核接口：管理员去审核

审核的前置条件：
    1、管理员登录（类级别前置）

    2、普通用户的角色添加项目
        1)、普通用户登录（类级别的前置）
        2)、创建一个项目（用例级别前置）

"""
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


@ddt
class TestAudit(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'audit')
    cases = excel.read_data()
    db = HandleDB()

    @classmethod
    def setUpClass(cls) -> None:
        url = conf.get('env', 'base_url') + "/member/login"
        # -----------------------管理员登录-----------------------
        # 1、准备登录的数据
        params = {
            "mobile_phone": conf.get("test_data", "admin_mobile"),
            "pwd": conf.get("test_data", "admin_pwd")
        }
        headers = eval(conf.get("env", "headers"))
        # 2、请求登录接口
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # 3、提取token，放到请求头中
        admin_token = jsonpath(res, '$..token')[0]
        headers["Authorization"] = "Bearer " + admin_token
        cls.admin_headers = headers
        # 4、提取用户id
        cls.admin_member_id = jsonpath(res, '$..id')[0]

        # ----------------------普通用户登录-----------------------
        # 1、准备登录的数据
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

    def setUp(self) -> None:
        """用例级别前置:添加项目"""
        # 第一步：准备数据
        url = conf.get('env', 'base_url') + '/loan/add'
        params = {"member_id": self.member_id,
                  "title": "借钱实现财富自由",
                  "amount": 2000,
                  "loan_rate": 12.0,
                  "loan_term": 3,
                  "loan_date_type": 1,
                  "bidding_days": 5}
        # 第二步：请求添加项目接口
        response = requests.post(url=url, json=params, headers=self.headers)
        res = response.json()
        # print(res)
        # 第三步：提前项目id，保存为类属性
        TestAudit.loan_id = jsonpath(res, '$..id')[0]

    @list_data(cases)
    def test_audit(self, item):
        # 第一步：准备数据
        url = conf.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestAudit)

        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method'].lower()
        row = item['case_id'] + 1

        # 第二步：请求接口
        response = requests.request(method=method, url=url, json=params, headers=self.admin_headers)
        res = response.json()
        print("预期结果：", expected)
        print("实际结果:", res)

        # 判断是否是审核通过的用例，并且审核成功，如果是则保存为id为审核通过的项目id
        if item['title'] == '审核通过' and res['msg'] == 'OK':
            TestAudit.pass_loan_id = self.loan_id

        # 第三步：断言
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if item['check_sql']:
                sql = item['check_sql'].format(self.loan_id)
                status = self.db.find_one(sql)[0]
                print('数据库该项目状态为：', status)
                self.assertEqual(expected['status'], status)

        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="不通过")
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--【{}】--执行成功".format(item['title']))
            self.excel.write_data(row=row, column=8, value="通过")
