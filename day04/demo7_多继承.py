"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""

"""
多继承：同时继承多个父类(了解即可)
"""


class BaseA:
    A = 100

    def func(self):
        print("----A----func")


class BaseB:
    B = 200

    def func(self):
        print("----B----func")


class MyClass(BaseA, BaseB):
    pass


m = MyClass()
m.func()
