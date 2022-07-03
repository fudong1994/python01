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

# 创建一个会话对象(使用这个session对象去发送请求，会自动记录请求的cookie信息，下一次请求会自动化添加cookie)
s = requests.session()
# # 请求地址
url = 'https://v4.ketangpai.com/UserApi/login'

# 请求参数：
params = {
    "email": "1406615758@qq.com",
    "password": "WFD19940918qw",
    "remember": 0
}
# data:专门用来传递表单类型的参数（content-type: application/x-www-form-urlencoded; charset=UTF-8）
response = s.post(url=url, data=params)
print(response.json())

# 课堂派获取课程内容的接口
url = "https://www.ketangpai.com/CourseApi/lists"
response = s.get(url=url)
print(response.text)
