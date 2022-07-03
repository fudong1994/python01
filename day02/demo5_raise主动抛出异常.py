"""
# @Time : 2022/5/16 0016   20:51
# @File : demo4_assert断言
# @Project : python01
# @Content :
"""

"""
raise:主动抛出异常
"""


# raise NameError("XXX没定义")

# raise ValueError

# ------------raise的应用场景------------
# 限制参数的类型，不是对应的类型主动抛出错误
def add(a, b):
    if not isinstance(a, int):
        raise ValueError("a只能是int类型")
    if not isinstance(b, int):
        raise ValueError("b只能是int类型")
    return a + b


# res = add(5, "bb")
# print(res)
