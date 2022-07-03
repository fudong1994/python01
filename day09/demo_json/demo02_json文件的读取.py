"""
# @Time : 2022/5/28 0028   20:49
# @File : demo01_json数据
# @Project : python01
# @Content :
"""

import json

with open("data.json", mode='r', encoding='utf-8') as f:
    # 读取文件中的json数据并自动化转换成py中相关的数据类型
    res = json.load(f)
print(res, type(res))
print(res['data'], type(res['data']))
