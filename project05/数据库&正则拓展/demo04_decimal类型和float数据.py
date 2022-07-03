from decimal import Decimal

a = 10
b = 10.10
# assert a == b

# 定义decimal类型的数据
res = Decimal('10.10')

assert b == float(res)