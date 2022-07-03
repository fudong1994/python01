"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""

"""

作用：子类通过继承可以获得父类的属性和方法，提高开发效率和代码复用率（__开头的私有属性和方法除外）

"""


class BasePhone:
    attr = "移动电话"
    __attr2 = "1000"

    def __init__(self, name):
        self.name = name

    def call(self):
        print(f"{self.name}打电话的功能")


class PhoneV2(BasePhone):

    def __init__(self, name, price):
        # 重写方法方式一：类名.方法名(self,)
        # BasePhone.__init__(self, name)

        # 重写方法方式二：super().方法()
        super().__init__(name)
        self.price = price

    def send_mag(self):
        print("发送短信")

    def music(self):
        print("放音乐")


p = PhoneV2("诺基亚N95", 5880)
p.call()
print(p.attr, p.price)
