"""
6、猜数字游戏
猜数字游戏：
1.系统随机生成一个1～10的数字；
2.用户共有5次机会猜；
3.如果用户猜测数字大于系统给出的数字，打印"too big"
4.如果用户猜测数字小于系统给出的数字，打印"too small"
5.如果用户猜测的数字等于系统给出的数字，打印"恭喜中奖"，并退出循环
"""

import random  # 导入 随机函数模块

print("""猜数字游戏：
1.系统随机生成一个1～15的数字；
2.用户共有3次机会猜；
3.如果用户猜测数字大于系统给出的数字，打印"too big"
4.如果用户猜测数字小于系统给出的数字，打印"too small"
5.如果用户猜测的数字等于系统给出的数字，打印"恭喜中奖"，并退出循环
""")

'''
for j in range(1,101):
    print('这是你的第{}次游戏'.format(j),'*****************我是淫荡的分割线***********************')
'''

act = random.randint(1, 15)

for i in range(0,5):
    exp = int(input('请输入数字:\n'))
    if exp > act:
        print("too big,还能再输入{}次".format(4 - i))
    elif exp < act:
        print("too small,还能再输入{}次".format(4 - i))
    else:
        print("恭喜猜对了")
        break

else:
    print("机会全部用完了。GAMEOVER,，实际数字是{}".format(act))
