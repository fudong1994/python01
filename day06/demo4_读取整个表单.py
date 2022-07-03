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

# 获取excel中第一行数据
title = [i.value for i in res[0]]
cases = []
# 遍历第一行以外所有的行
for item in res[1:]:
    # 获取该行的数据放到列表中
    data = [i.value for i in item]
    # 将第一行的数据和当前这行数据打包成字典
    dit = dict(zip(title, data))
    # 把字典添加到cases这个列表中
    cases.append(dit)
print(cases)
