"""
# @Time : 2022/5/28 0028   20:18
# @File : python读取yaml文件
# @Project : python01
# @Content :
"""

import yaml

with open('cases.yaml', mode='r', encoding='utf-8') as f:
    res = yaml.load(f, Loader=yaml.Loader)

print(res, type(res))
