"""
# @Time : 2022/6/7 0007   20:33
# @File : demo_02路径处理
# @Project : project02
# @Content :
"""
import os

# 获取项目的根目录
base_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取用例数据文件夹所在目录的绝对路径
data_dir = os.path.join(base_path1, 'datas')
print(data_dir)
