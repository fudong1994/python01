import re

# 通过正则表达式规则匹配需求的数据
str1 = "asdafa16588548548sfda15821873878qwe123qw15655845847eqwe"
# res = re.findall('\d{11}', str1)
res = re.findall('165\d{8}', str1)
print(res)

"""
正则表达式的语法
"""
# ---------------------单字符(元字符)：表示单个字符-----------------------
s1 = '460986521354asdSADFKascdassa * &%（￥'
# \d：表示一个数字
res1 = re.findall('\d', s1)
print(res1)

# \D：表示一个非数字
res1 = re.findall('\D', s1)
print(res1)

# \s：表示一个空白字符
res1 = re.findall('\s', s1)
print(res1)

# \S：表示一个非空白字符
res1 = re.findall('\S', s1)
print(res1)

# \w：表示一个单词字符(数字、字母、下划线)
res1 = re.findall('\w', s1)
print(res1)

# \W：表示一个非单词字符(除数字、字母、下划线的所有字符)
res1 = re.findall('\W', s1)
print(res1)

# . ：表示任意字符(通配符)
res1 = re.findall('.', s1)
print(res1)

# [] ：举例匹配的单字符
# res1 = re.findall('[1-3]', s1)
# res1 = re.findall('[ac23]', s1)
res1 = re.findall('[0-9a-zA-Z]', s1)
print(res1)

