"""
# @Time : 2022/5/28 0028   19:47
# @File : demo01_python中操作配置文件
# @Project : python01
# @Content :
"""

from configparser import ConfigParser

# 第一步：创建一个配置文件解释器对象
cg = ConfigParser()

# 第二步：读取配置文件中的内容到文件解析器中
cg.read('musen.ini', encoding='utf-8')

# 第三步：读取配置类容
# get:读取的内容是str类型
res = cg.get('logging', 'port')
print(res, type(res))

# getint:读取出来的是int类型
res2 = cg.getint('logging', 'port')
print(res2, type(res2))

# getboolean:读取出来的是布尔类型
# cg.getboolean()

# getfloat:读取出来的是浮点类型的数据
# cg.getfloat()
