"""
# @Time : 2022/5/24 0024   16:49
# @File : demo_01excel数据处理的封装
# @Project : python01
# @Content :
"""

"""

        
"""

import openpyxl

workbook = openpyxl.load_workbook('D:\pythonworkspace\python01\day07\cases.xlsx')
sh = workbook['Sheet2']

# excel数据写入
sh.cell(row=1, column=1, value="python666")
workbook.save('D:\pythonworkspace\python01\day07\cases.xlsx')
