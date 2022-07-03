"""
# @Time : 2022/5/28 0028   20:49
# @File : demo01_json数据
# @Project : python01
# @Content :
"""

import json

# --------------------------python转json-----------------------
dic = {"aa": None, "bb": "python", "cc": True, "dd": False, "ee": [11, 22, 33]}
# 将python数据(列表或字典)转换成json
res = json.dumps(dic)
print(res, type(res))

print(json.dumps(None))
res = json.dumps(True)
print(res, type(res))

# ---------------------json转python------------------------------
s_json = '{"aa": null, "bb": "python", "cc": true, "dd": false, "ee": [11, 22, 33]}'
# 将字符串转换成对应的python数据
res = json.loads(s_json)
print(res, type(res))

# json模块总结：
#     load:读取json文件转换为对应的python数据
#     loads:将json字符串转换成对应的python数据
#     dumps：将python数据转换为json字符串