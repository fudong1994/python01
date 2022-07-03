import re

"""

"""


class TestData:
    id = 10
    name = 'yanzu'
    data = '0011'
    title = 'OK'


s = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'

# findall:匹配所有符合规则的数据，以列表返回
res = re.findall('#.+?#', s)
print(res)

# search:匹配第一个符合规则的数据，返回一个匹配对象，没有匹配到返回None
res = re.search('#(.+?)#', s)
print(res)
# group:提取匹配对象中的内容
item = res.group()
print('被替换的内容：', item)
attr = res.group(1)
print('替换的属性名：', attr)
value = getattr(TestData, attr)
print('获取出来的类属性值：', value)
# 进行替换
s = s.replace(item, str(value))
print(s)

print('----------------------------------------------------')
res = re.search('#(.+?)#', s)
print(res)
# group:提取匹配对象中的内容
item = res.group()
print('被替换的内容：', item)
attr = res.group(1)
print('替换的属性名：', attr)
value = getattr(TestData, attr)
print('获取出来的类属性值：', value)
# 进行替换
s = s.replace(item, str(value))
print(s)

print('----------------------------------------------------')
res = re.search('#(.+?)#', s)
print(res)
# group:提取匹配对象中的内容
item = res.group()
print('被替换的内容：', item)
attr = res.group(1)
print('替换的属性名：', attr)
value = getattr(TestData, attr)
print('获取出来的类属性值：', value)
# 进行替换
s = s.replace(item, str(value))
print(s)

print('----------------------------------------------------')
res = re.search('#(.+?)#', s)
print(res)
# group:提取匹配对象中的内容
item = res.group()
print('被替换的内容：', item)
attr = res.group(1)
print('替换的属性名：', attr)
value = getattr(TestData, attr)
print('获取出来的类属性值：', value)
# 进行替换
s = s.replace(item, str(value))
print(s)
