import re

"""
正则表达式的语法
"""
# -------------------------表示数量--------------------------

s1 = '1234asdsad5654223.55464654YY87978t98666545'
# {n},表示前一个字符出现n次
res = re.findall('\d{4}', s1)
print(res)

# {n,},表示前一个字符出现n次以上
res = re.findall('\d{4,}', s1)
print(res)

# {n,m},表示前一个字符出现n到m次
res = re.findall('\d{4,6}', s1)
print(res)

res = re.findall('\d{4,6}?', s1)
print(res)

# 贪婪模式的应用
# 默认是开启贪婪模式去匹配的，贪婪模式关闭：表示数量的范围后面加？
# 关闭贪婪模式的应用
s = '{"id": "##", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'
res = re.findall('#.{1,}?#', s)
print(res)

# +：表示一次以上（等同于{1,}）
res = re.findall('#.+?#', s)
print(res)

# *:表示0次以上
res = re.findall('#.*?#', s)
print(res)
