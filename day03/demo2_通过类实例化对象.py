"""
# @Time : 2022/5/17 0017   11:37
# @File : demo1_类的定义
# @Project : python01
# @Content :
"""
"""
1、通过类实例化对象
    语法：
        对象 = 类名()
        
万物皆对象：所有的数据都是对象  
    字符串：str类型的对象
    列表：list类型的对象
    函数：函数类型的对象   
    整数：int类型的对象   
"""


class Cat:
    pass


# 通过猫类创建对象
coffee = Cat()
jingle = Cat()

print(coffee, type(coffee))
print(jingle, type(jingle))


class PersonClass(object):
    pass


# 通过人类创建对象
wen = PersonClass()
Try = PersonClass()
print(wen, type(wen))
print(Try, type(Try))
