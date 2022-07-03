import re

"""
表示边界

字符串的边界：
    ^:表示字符串的开头（起始位置）
    $:表示字符串的结尾（终止位置）
    
单词边界：
    \b:表示单词边界
    \B:表示非单词边界 

"""
# -------------------------表示边界--------------------------
s = '123python456java123c++123'

# ^:表示字符串的开头（起始位置）
res = re.findall('^123', s)
print(res)

# $:表示字符串的结尾（终止位置）
res = re.findall('123$', s)
print(res)

s = 'python is good?javapython'

# \b:表示单词边界
res = re.findall(r'\bpython', s)
print(res)
res = re.findall(r'python\b', s)
print(res)

# \B:表示非单词边界
res = re.findall(r'\Bpython', s)
print(res)
