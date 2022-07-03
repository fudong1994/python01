import unittest
import os
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handler_log import my_log
from common.tools import replace_data


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apicases.xlsx"), "login")
    # 读取用例数据
    cases = excel.read_data()
    # 项目的基本地址
    base_url = conf.get("env", "base_url")
    # 请求头
    headers = eval(conf.get('env', 'headers'))

    @list_data(cases)
    def test_login(self, item):
        # 第一步、准备用例数据
        # 1、接口地址
        url = self.base_url + item["url"]
        # 2、请求参数
        item['data'] = replace_data(item['data'], TestLogin)

        params = eval(item['data'])
        # 3、请求头
        # 4、获取请求方法，并转换成小写
        method = item['method'].lower()
        # 5、预期结果
        expected = eval(item['expected'])
        row = item['case_id'] + 1
        # 第二步、请求接口，获取实际结果
        # requests.post(url=url, json=params, headers=self.headers)
        response = requests.request(method, url=url, json=params, headers=self.headers)
        res = response.json()
        # 第三步、断言
        print("预期结果:", expected)
        print("实际结果：", res)
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
        except AssertionError as e:
            # 回写结果到excel
            self.excel.write_data(row=row, column=8, value="不通过")
            # 记录日志
            my_log.error("用例--【{}】--执行失败".format(item['title']))
            my_log.exception(e)
            raise e
        else:
            my_log.info("用例--【{}】--执行通过".format(item['title']))
            self.excel.write_data(row=row, column=8, value="通过")
