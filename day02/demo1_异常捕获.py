"""
# @Time : 2022/5/16 0016   19:05
# @File : demo01_异常捕获
# @Project : python01
# @Content :
"""

"""
try
    有可能会出错的代码
except:
    当try里的代码执行出现错误时，会执行except，这里进行异常处理
    
try
    有可能会出错的代码
except 异常类型 as e:
    pass    
    
"""
# -------------捕获所有的异常类型----------------
# try:
#     number = float(input("请输入数字:"))
#     print(number)
# except Exception as e:
#     # 可以在这里进行异常处理
#     # print("当try里的代码执行出现错误时，会执行except")
#     print("你输入的不是数字")
#     print("错误信息：", e)


# --------------捕获指定的异常类型-----------------
dic = {"a": 1}
# print(name) NameError: name 'name' is not defined
# print(dic["b"]) KeyError: 'b'

# try:
#     print("------1-----")
#     print(name)
#     print("------2-----")
#     print(dic["b"])
# except NameError as e:
#     print(e)

# -----------捕获多个异常，不同异常不同处理----------------
try:
    print("------1-----")
    # print(name)
    print("------2-----")
    print(dic["b"])
except NameError as e:
    print("NameError的处理方式", e)
except KeyError as e:
    print("KeyError的处理方式", e)
