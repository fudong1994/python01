"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""

"""
动态属性设置:setattr()
    参数1：对象(类)
    参数2：属性名
    参数3：属性值

动态获取属性：getattr()
    参数1:对象(类)
    参数2：属性名
    参数3：(非必传)设置一个属性不存在时返回的默认值
    
动态删除属性：delattr()
    参数1：对象(类)
    参数2：属性名

判断属性是否存在：hasattr()
    参数1：对象(类)
    参数2：属性名

"""


# --------------------动态属性设置-----------------------
# class MyClass:
#     attr = 100


# print(MyClass.__dict__) # 打印这个类的所有属性

# 在代码执行的过程中给类添加属性
# 方式一：通过类名
# MyClass.name = "彦祖"
# print(MyClass.name)

# 方式二：setattr()
# key = 'name'
# value = '彦祖'
# setattr(MyClass, key, value)
# print(MyClass.__dict__)

# 需求：把字典中的键值对设置为类的属性和属性值
# data = {"name": "彦祖", "age": 18, "sex": "男"}
# for k, v in data.items():
#     setattr(MyClass, k, v)
# print(MyClass.__dict__)

# 给对象动态赋值对象属性和属性值
# m = MyClass()
# data = {"name": "彦祖", "age": 18, "sex": "男"}
# for k, v in data.items():
#     setattr(m, k, v)
# print(m.__dict__)
# print(m.name)
# print(m.age)
# print(m.sex)

# -----------------------动态获取属性--------------------
# class MyClass:
#     attr = 100
#     name = "彦祖"
#     age = 18


# key2 = "attr"
# res = getattr(MyClass, key2)
# print(res)

# key = input("请输入要获取的属性:")
# res = getattr(MyClass, key, "属性不存在，请检查")
# print(res)

# ----------------------动态删除属性--------------------
# class MyClass:
#     attr = 100
#     name = "彦祖"
#     age = 18


# key = input("请输入要删除的属性:")
# delattr(MyClass, key)
# print(MyClass.__dict__)

# -------------------动态检查属性是否存在---------------
class MyClass:
    attr = 100
    name = "彦祖"
    age = 18


res = hasattr(MyClass, "attr")
print(res)
