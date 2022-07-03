import requests

"""
#==========================参数类型：content-type: application/x-www-form-urlencoded; charset=UTF-8==================
课堂派演示登录接口
https://openapiv5.ketangpai.com//UserApi/login
参数：content-type: application/x-www-form-urlencoded; charset=UTF-8
    email: "账号"
    password: "密码"
    remember: "0"
Content-Type: content-type: application/x-www-form-urlencoded; charset=UTF-8
"""

# # 请求地址
# url = 'https://v4.ketangpai.com/UserApi/login'
#
# # 请求参数：
# params = {
#     "email": "1406615758@qq.com",
#     "password": "WFD19940918qw",
#     "remember": 0
# }
# # data:专门用来传递表单类型的参数（content-type: application/x-www-form-urlencoded; charset=UTF-8）
# response = requests.post(url=url, data=params)
# print(response.json())

# =========================参数类型：application/json=================================
# 项目中的注册接口：post请求
# 请求地址
url = "http://api.lemonban.com/futureloan/member/register"
# 请求头
head = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}
# 请求参数
params = {
    "mobile_phone": "15821873878",
    "pwd": "12345678",
    "type": 0
}
# 发生请求的时候添加请求头使用headers
# 参数类型是json的情况下，需要用json来传递参数
response = requests.post(url=url, headers=head, json=params)
print(response.text)

# ============================get请求参数(查询字符串参数)==========================
# 方式一：查询字符串参数，可以直接拼接在url上
url1 = "http://api.lemonban.com/futureloan/loans?pageIndex=1&pageSize=10"
head1 = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}
response1 = requests.get(url=url1, headers=head1)
print(response1.text)

# 方式二：params进行传递
url2 = "http://api.lemonban.com/futureloan/loans"
hea2 = {
    "X-Lemonban-Media-Type": "lemonban.v1"
}
params = {
    "pageIndex": 1,
    "pageSize": 10
}
response2 = requests.get(url=url2, params=params, headers=hea2)
print(response2.text)

# ===================== content-type: from/data(了解即可)=======================
# requests.post(url="", files="")
