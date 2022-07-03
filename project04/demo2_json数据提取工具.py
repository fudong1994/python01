"""
jsonpath方法需要两个 参数
参数1：数据
参数2：jsonpath表达式



注意点：
    1.如果没有匹配到数据返回False
    2.匹配到数据则返回包含数据的列表


jsonpath表达式语法
$               ----->根节点
.               ----->子节点
..              ----->选择子孙节点(不考虑层级)
[]              ----->选择子节点/选择索引
[,]             ----->选择多个字段
@               ----->代表当前选中的节点（和条件过滤一起使用）
[?(过滤条件)]     ----->通过条件过滤数据

"""
import requests
from jsonpath import jsonpath

# response = requests.get("https://www.xfz.cn/api/website/partners/")
# print(response.json())

data = {'code': 200,
        'data': [{'photo': 'https://static-image.xfz.cn/1454046552_487.png',
                  'create_time': '2016-01-29 13:49:13',
                  'link': 'http://www.ehoutai.com/',
                  'uid': 7,
                  'name': '易后台'},
                 {'photo': 'https://static-image.xfz.cn/1454046135_474.png',
                  'create_time': '2016-01-29 13:42:15',
                  'link': 'http://www.sanjieke.com/',
                  'uid': 4,
                  'name': '三节课'},
                 {'photo': 'https://static-image.xfz.cn/1454046053_122.png',
                  'create_time': '2016-01-29 13:40:53',
                  'link': 'https://www.aliyun.com/',
                  'uid': 1,
                  'name': '阿里云'},
                 {'photo': 'https://static-image.xfz.cn/1454047318_361.png',
                  'create_time': '2016-01-29 14:01:59',
                  'link': 'http://xmanlegal.com/',
                  'uid': 8,
                  'name': '未来法律'}]}

data2 = {'code': 0,
         'msg': 'OK',
         'data': {'id': 323467,
                  'leave_amount': 28000.0,
                  'mobile_phone': '15655658548',
                  'reg_name': '小柠檬',
                  'reg_time': '2022-06-07 23:41:39.0',
                  'type': 1,
                  'token_info': {'token_type': 'Bearer',
                                 'expires_in': '2022-06-09 21:48:04',
                                 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjMyMzQ2NywiZXhwIjoxNjU0NzgyNDg0fQ.kuYVFBihOqQeF0COjO1HZzVwc9BGYR5oCLWlY8_e6qfHkWy2QmRdJwIBBn29-x4I_fZuAhTeaeRroJu1AMgLIw'}},
         'copyright': 'Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved'}

# 选择子节点
# print(jsonpath(data2, "$.code"))
# print(jsonpath(data2, "$[code]"))

# 通过索引选择列表中的数据
print(jsonpath(data, "$.data[1]"))
print(jsonpath(data, "$.data[1].name"))

# 选择多个字段
print(jsonpath(data, "$.data[0][uid,name,photo]"))

# 通过条件过滤查找
print(jsonpath(data, "$.data[?(@.uid==1)]"))
print(jsonpath(data, "$.data[?(@.uid==8)].link"))
print(jsonpath(data, "$.data[?(@.name=='三节课')]"))


# token = jsonpath(data2, "$..token")
# print(token)
