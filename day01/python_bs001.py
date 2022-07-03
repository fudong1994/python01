# print('hellow World')

# def cft(data=["{'a':11,'b':2}", "[11,22,33,44]"]):
#     res = []
#     for str1 in data:
#         dict1 = eval(str1)
#         res.append(dict1)
#     return res
#
#
# if __name__ == '__main__':
#     list1 = cft()
#     print(list1)

# 打印99乘法表
for i in range(9):
    for j in range(i + 1):
        print("{}x{}={:<3} ".format(j + 1, i + 1, (i + 1) * (j + 1)), end="")
    print()

print()

# 打印99乘法表，倒序
for i in range(9):
    for j in range(9-i):
        print("{}x{}={:<3} ".format(j+1, 9 - i, (9 - i) * (j+1)), end="")
    print()

# 列表推导式
list1 = ["我是吴彦祖{}号".format(i) for i in range(1, 10, 2)]
print(list1)

# 把字典的值*10，打印出来
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for i in dict1:
    dict1[i] = dict1[i] * 10
print(dict1)


# 根据传入的计算方法计算
def func(a, b, method):
    if method == "+":
        print("{}+{}={}".format(a, b, a + b))
    elif method == "-":
        print("{}-{}={}".format(a, b, a - b))
    elif method == "*":
        print("{}*{}={}".format(a, b, a * b))
    elif method == "/":
        print("{}/{}={:.2f}".format(a, b, a / b))
    else:
        print("传入的计算方式有误")


func(5, 6, "+")
