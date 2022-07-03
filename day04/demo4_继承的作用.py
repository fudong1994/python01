"""
# @Time : 2022/5/23 0023   14:24
# @File : demo1_私有属性
# @Project : python01
# @Content :
"""

"""
作用：子类通过继承可以获得父类的属性和方法，提高开发效率和代码复用率（__开头的私有属性和方法除外）

"""


# 继承
class BasePhone:
    def call(self):
        print("打电话的功能")


class PhoneV2(BasePhone):

    def send_mag(self):
        print("发送短信")

    def music(self):
        print("放音乐")


class PhoneV3(PhoneV2):

    def pay(self):
        print("支付")

    def game(self):
        print("玩游戏")


xiaomi = PhoneV3()
xiaomi.call()
xiaomi.send_mag()
xiaomi.music()
xiaomi.pay()
