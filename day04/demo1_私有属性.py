"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""
"""
私有属性：仅供类的内部使用
    _单下划线开头：表示这是一个私有属性（没有真正的私有化，外部依然可以调用）
    __双下划线开头：表示这是一个私有属性（类外部不可以调用）
    
私有方法：
    _单下划线开头：表示这是一个私有方法（没有真正的私有化，外部依然可以调用）
    __双下划线开头：表示这是一个私有方法（类外部不可以调用）       
"""


class MyClass:
    _attr = 100
    __name = "彦祖"

    def __get_info(self):
        print("---get_info")

    def __get_name(self):
        print("---get_name")

    def func(self):
        print(self.__name)


b = MyClass()

# print(b._attr)
# print(b.__name)
b.func()