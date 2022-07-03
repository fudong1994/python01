import requests

# 项目中的注册接口：post请求
# url = "http://api.lemonban.com/futureloan/member/register"
# response = requests.post(url=url)
# print(response.text)

"""
课堂派演示登录接口
https://openapiv5.ketangpai.com//UserApi/login
参数：content-type: application/x-www-form-urlencoded; charset=UTF-8
    email: "账号"
    password: "密码"
    remember: "0"
Content-Type: content-type: application/x-www-form-urlencoded; charset=UTF-8
"""

# 请求地址
url = 'https://v4.ketangpai.com/UserApi/login'

# 请求参数：
params = {
    "email": "1406615758@qq.com",
    "password": "WFD19940918qw",
    "remember": 0
}
# data:专门用来传递表单类型的参数（content-type: application/x-www-form-urlencoded; charset=UTF-8）
response = requests.post(url=url, data=params)
print(response.json())

# get请求
# requests.get()

# put请求
# requests.put()

# 常用的请求类型  requests中都封装了请求方法，直接使用requests去调用就行了
