"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""
"""
实例方法：
        1.只能通过对象调用（第一个参数self,代表对象本身）
        2.适用场景：方法内部如果要使用对象的属性或者方法，就要定义成对象方法

类方法的定义：要先使用@classmethod声明
类方法:（第一个参数cls,代表类本身）
        1.可以通过类调用，也可以通过对象调用
        2.适用场景：方法内部只使用类属性或者类方法（不需要使用对象属性和方法）
        
静态方法的定义：要先使用@staticmethod声明
静态方法：
       1.可以通过类调用，也可以通过对象调用
       2.适用场景：方法内部（既不需要使用类属性和类方法也不使用对象属性和对象方法）
"""


class MyClass:

    def func(self):
        print("---func---实例方法")

    @classmethod
    def func_cls(cls):
        print("---func_cls---实例方法")

    @staticmethod
    def func_static():
        print("---func_static---实例方法")


class MyTest:
    attr = 100

    def __init__(self, name):
        self.name = name

    def func1(self):
        print(self.name)

    @classmethod
    def func2(cls):
        print(cls.attr)

    @staticmethod
    def func3():
        print("静态方法")
