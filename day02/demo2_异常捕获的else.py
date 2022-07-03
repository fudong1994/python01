"""
# @Time : 2022/5/16 0016   19:40
# @File : demo2_异常捕获
# @Project : python01
# @Content :
"""

"""
try:
    有可能会出错的代码
except:
    当try里的代码执行出现错误时，会执行except，这里进行异常处理
else:
    try的代码没有报错，会执行else中的代码
finally:
    不管try中代码出不出错，都会执行
"""

# 读取data.txt的文件，并写入 python 你好
# try:
#     with open(file="data.txt", mode="r", encoding="utf_8") as f:
#         res = f.read()
# except:
#     print("data.txt这个文件不存在")
# else:
#     print(res)
#
# with open(file="data.txt", mode="w", encoding="utf_8") as f:
#     f.write("python 你好")

# -------------------finally----------------
name = "彦祖"
try:
    # print(name)
    res = "11" + 11  # 异常没有捕获到，仍然会执行finally
except NameError:
    print("代码出错了")
else:
    print("代码没出错")
finally:
    print("finally执行了")

print("9999999999999999")  # 此处不执行了
