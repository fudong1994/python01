"""
# @Time : 2022/5/24 0024   14:41
# @File : __init__.py
# @Project : python01
# @Content :
"""

import openpyxl

# ----------------读取表单所有的数据----------------
workbook = openpyxl.load_workbook("case.xlsx")
sh = workbook["yanzu"]

# rows:按行获取表单中所有的格子，每一行放到一个元组中
res = list(sh.rows)

# title = res[0]
# print(title)
# n = []
# for i in title:
#     n.append(i.value)

# 获取excel中第一行数据
title = [i.value for i in res[0]]
# print(title)
cases = []
for item in res[1:]:
    data = [i.value for i in item]
    dit = dict(zip(title, data))
    cases.append(dit)
print(cases)
# r2 = [i.value for i in res[1]]
# print(r2)
# print(dict(zip(title, r2)))

# r3 = [i.value for i in res[2]]
# print(r3)
# print(dict(zip(title, r3)))

# r4 = [i.value for i in res[3]]
# print(r4)
# print(dict(zip(title, r4)))
