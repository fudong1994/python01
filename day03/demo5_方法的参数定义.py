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

二、方法：定义在类里面的函数
    方法中的参数除self，其他的参数传递跟函数是一样的
    方法中也是使用return来返回数据的
"""


class Cat:
    leg = 4
    tail = 1
    eye = 2

    def func(self, addr, number):
        # print(self.name)
        print("{}正在{}抓{}只老鼠".format(self.name, addr, number))
        return "3只老老鼠"


# 通过猫类创建对象
coffee = Cat()
coffee.name = "加菲猫"
jingle = Cat()
jingle.name = "叮当猫"

# 通过对象调用方法
coffee.func('树上', 2)
res = coffee.func('树上', 2)
print(res)
jingle.func('小黑屋', 4)
