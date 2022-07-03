"""
# @Time : 2022/6/7 0007   22:41
# @File : demo01_requests模块的基本使用
# @Project : project03
# @Content :
"""

import requests

# 发送一个简单的请求

url = "http://www.lemonban.com/"

response = requests.get(url=url)

# ------------------------------------响应信息的获取------------------------------------------
# 获取返回的响应状态码
print(response.status_code)

# 获取响应头：
print(response.headers)

# 获取响应体：
# 方式一：自动识别返回内容的编码，进行解码（可能会出现乱码）
# 对返回的任意类型数据都可以用该方式去获取
# print(response.text)

# 方式二：指定编码对返回内容编码
# print(response.content.decode('utf-8'))

# 方式三：只能在返回数据是json的情况下才能使用该方法（接口测试常用）
# 会自动将返回的json转换成pythonl类型数据
# print(response.json()) # 返回的不是json会报错

# ------------------------------------请求信息的获取----------------------------------
# 1、获取请求头
print(response.request.headers)

# 2、获取请求体
print(response.request.body)
