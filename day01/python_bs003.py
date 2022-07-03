"""
# @Time : 2022/5/14 0014   21:45
# @File : python_bs003
# @Project : python01
# @Content :
"""

""""""
"""

注册功能
"""

users = [{'user': 'python35', 'password': '123456'}]


def resigter(username, password1, password2):
    # 判断是否有参数为空
    if not username and not password1 and not password2:
        return {"code": 0, "msg": "所有参数不能为空"}

    # 注册功能
    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['user']:
            # 账号存在
            return {"code": 0, "msg": "该账号已经存在"}

    else:
        if password1 != password2:
            # 两次密码不一致
            return {"code": 0, "msg": "两次密码不一致"}
        else:
            # 账号不存在，密码一致，判断账号密码长度是否大于6位小于18位
            if 6 <= len(username) <= 18 and 6 <= len(password1) <= 18:
                # 注册账号
                users.append({'user': username, 'password': password2})
                return {"code": 1, "msg": "账号注册成功！"}
            else:
                # 账号密码长度不对，注册失败
                return {"code": 0, "msg": "账号或者密码长度必须在6-18位之间"}


if __name__ == '__main__':
    res = resigter('python1', '111222333', '111222333')
    print(res)