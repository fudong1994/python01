"""
# @Time : 2022/5/15 0015   10:17
# @File : python_bs004
# @Project : python01
# @Content :
"""

# f = open(file="biji.txt", mode="r", encoding="utf-8")
# f.close()

with open(file="biji.txt", mode="r", encoding="utf-8") as f:
    # f.write("这也太秀了吧\n" * 10)
    res = f.readlines()

res2 = {}
for i, j in enumerate(res):
    key = "data{}".format(i + 1)
    values = j.replace("\n", "")
    res2[key] = values
print(res2)