"""
同一个接口不同用例返回的字段不一样

"""
import unittest


class TestDemo(unittest.TestCase):

    def test_demo(self):
        # 实际结果
        res = {"code": 0, "msg": "OK", "time": "20220614"}
        # 预期结果
        expected = {"code": 0, "msg": "OK"}

        # assert res['code'] == expected['code']
        # assert res['msg'] == expected['msg']
        self.assertEqual(expected['code'], res['code'])
        self.assertEqual(expected['msg'], res['msg'])

    def assertDictIn(self, expected, res):
        for k, v in expected.items():
            if res.get(k) == v:
                print("预期结果正确")
            else:
                raise AssertionError("{} not in {}".format(expected, res))
