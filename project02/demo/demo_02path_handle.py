"""
# @Time : 2022/6/7 0007   20:33
# @File : demo_02路径处理
# @Project : project02
# @Content :
"""
import os

# os.path.abspath:获取绝对路径
# p1 = os.path.abspath('code.txt')
# print(p1)

res = os.path.abspath(__file__)

# os.path.dirname获取所在目录的路径
path1 = os.path.dirname(res)
# 获取当前文件的项目根目录
base_path = os.path.dirname(path1)
print(base_path)

base_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_path1)