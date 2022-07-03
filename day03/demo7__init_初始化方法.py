"""
# @Time : 2022/5/17 0017   11:37
# @File : demo1_类的定义
# @Project : python01
# @Content :
"""

# -----------------init---------------
# 魔术方法：双下划线开头跟双下划线结尾的方法，不需要手动调用，特地的时候会自动调用

"""
初始化方法__init__:在通过类创建对象的时候自动调用

"""


class Persion:
    def __init__(self, name, age, sex):
        # 在创建对象的时候，给对象设置对象属性
        self.name = name
        self.age = age
        self.sex = sex
        print("这是个__init__方法")


yanzu = Persion("彦祖", 18, "男")
print(yanzu.name)
print(yanzu.age)
print(yanzu.sex)
