"""
# @Time : 2022/5/17 0017   11:37
# @File : demo1_类的定义
# @Project : python01
# @Content :
"""
"""
特征：属性
行为：方法
    
类的方法和属性
一、属性：
    1、类属性:这类事物都具备这个属性，并且属性值是一样的
    类属性的定义：直接定义在类里面的变量
        
    2、对象(实例)属性：对象自己的特征
        实例属性的定义：对象.属性名 = 属性值
二、方法：定义在类里面的函数

三、self:代表的是对象本身
    哪个对象调用该方法，self代表的就是那个对象
"""


class Cat:
    # 类属性
    leg = 4
    tail = 1
    eye = 2

    def func(self):
        print(self.name)
        print("{}正在抓老鼠".format(self.name))

    def skill01(self):
        print("这个是爬树的功能")


# 通过猫类创建对象
coffee = Cat()
coffee.name = "加菲猫"

jingle = Cat()
jingle.name = "叮当猫"
# print(coffee.name)
# print(jingle.name)

# 通过对象调用方法
coffee.func()
jingle.func()
