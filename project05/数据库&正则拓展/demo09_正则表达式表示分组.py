import re

"""
表示分组
    ():分组提取
    |：表示多个匹配规则
"""
# -------------------------表示分组--------------------------
s = '{"id": "#id#", "name": "#name#", "data": "#data#", "title": "#title#", "aa": 11, "bb": 22}'

res = re.findall('#.+?#', s)
print(res)

res = re.findall('#(.+?)#', s)
print(res)

s2 = 'dsfdf223BBBaa123aa-aa456aa-aa789aaBBBasdwqae123asrd'

res = re.findall('BBB(.+?)BBB', s2)
print(res)

res = re.findall('aa(.+?)aa', s2)
print(res)

s3 = 'asdsdfas#user=lemonban-pwd=1234#asdfasdsdgsdfas.sdfsdfasfdasd#user=python-pwd=6666#sdsdfds'
res = re.findall(r'#user=(.+?)-pwd=(.+?)#', s3)
print(res)

# ----------------------表示多个匹配规则-------------------------
s = 'asd432python345java1234123'
res = re.findall('python|java', s)
print(res)

s2 = 'aaa@python@sadad#java#dsaf'
res = re.findall('@.+?@|#.+?#', s2)
print(res)
