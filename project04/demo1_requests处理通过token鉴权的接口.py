"""

第一步：登录，提取token，保存起来

第二步：访问需求鉴权的接口时，带上token


"""
import requests

# 第一步：登录，提取token，保存起来
# 登录接口的地址
url = "http://api.lemonban.com/futureloan/member/login"
# 登录接口的参数
params = {
    "mobile_phone": "15655658548",
    "pwd": "12345678"
}
# 请求头
header = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}
# 发生请求
response = requests.post(url=url, json=params, headers=header)
# print(response.text)
# 返回的json数据转换成python数据
res = response.json()
# print(type(res), res)
# 提取token的值
token = res['data']['token_info']['token']
print(token)
member_id = res['data']['id']

# 第二步：访问需求鉴权的接口时，带上token
# 充值接口地址
url2 = "http://api.lemonban.com/futureloan/member/recharge"
# 参数
params2 = {
    "member_id": member_id,
    "amount": 20000
}
# 请求头
header2 = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Authorization": "Bearer " + token
}

response2 = requests.post(url=url2, json=params2, headers=header2)
print(response2.json())