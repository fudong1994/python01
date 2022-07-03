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

"""


class Cat:
    leg = 4
    tail = 1
    eye = 2

    def func(self):
        print("这个是抓老鼠的功能")

    def skill01(self):
        print("这个是爬树的功能")


# 通过猫类创建对象
coffee = Cat()
coffee.name = "加菲猫"
coffee.age = "18个月"

jingle = Cat()
jingle.name = "叮当猫"
jingle.age = "50个月"

# ------------方法怎么使用-------------
coffee.func()
coffee.skill01()