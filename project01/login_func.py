"""
# @Time : 2022/5/23 0023   18:58
# @File : login_func
# @Project : python01
# @Content :
"""


def login_check(username=None, password=None):
    """
    登录函数的校验
    :param username:账号
    :param password:密码
    :return:结果（dict类型）
    """
    if username != None and password != None:
        if username == "python35" and password == "lemonban":
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有参数不能为空"}


if __name__ == '__main__':
    res = login_check("python35", "lemonban")
    print(res)
