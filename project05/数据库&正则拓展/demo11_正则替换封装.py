import re


class TestData:
    id = 10
    name = 'yanzu'
    data = '0011'
    title = 'OK'


s = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'

# search:匹配第一个符合规则的数据，返回一个匹配对象,没有匹配到返回None
while re.search('#(.+?)#', s):
    res = re.search('#(.+?)#', s)
    item = res.group()
    attr = res.group(1)
    value = getattr(TestData, attr)
    # 进行替换
    s = s.replace(item, str(value))

print(s)