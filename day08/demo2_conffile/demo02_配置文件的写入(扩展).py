"""
# @Time : 2022/5/28 0028   20:05
# @File : demo02_配置文件的写入(扩展)
# @Project : python01
# @Content :
"""

from configparser import ConfigParser

# 第一步：创建一个配置文件解释器对象
cp = ConfigParser()

# 第二步：读取配置文件中的内容到文件解析器中
cp.read('musen.ini', encoding='utf-8')

cp.set('mysql', 'name', 'musen')
cp.write(fp=open('musen.ini', mode='w', encoding='utf-8'))
