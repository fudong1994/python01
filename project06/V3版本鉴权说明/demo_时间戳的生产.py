from time import time

# 时间戳的获取
t = int(time())
print('当前的时间戳：', t)


# 签名的获取
# token的前50位 + 时间戳，然后进行RSA加密

token = 'asdasfsafsfdgdfhfggsdfsysdfsdfsdasdf.asdasfgadsag.asdafasdafadasfasdgasdfasdasdasd'
data = token[:50] + str(t)
