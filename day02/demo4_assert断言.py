"""
# @Time : 2022/5/16 0016   20:51
# @File : demo4_assert断言
# @Project : python01
# @Content :
"""

"""
assert:断言

预期结果：

实际结果：
"""
# 预期结果
expected = "注册成功"
# 实际结果
res = "注册失败"
try:
    assert expected == res
except AssertionError as e:
    print("断言不通过，用例执行不通过")
else:
    print("断言通过，用例执行成功")
