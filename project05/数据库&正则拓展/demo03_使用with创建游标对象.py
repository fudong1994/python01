import pymysql

# 1、连接数据库
con = pymysql.connect(host='api.lemonban.com',
                      port=3306,
                      user='future',
                      password="123456",
                      charset='utf8'
                      # cursorclass=pymysql.cursors.DictCursor:设置返回的数据为字典格式，默认是元组
                      )

# 2、创建游标对象(自动提交事务)pymysql 0.9.3
# with con as cur:

cur = con.cursor()
sql = "select * from futureloan.member limit 5"
res = cur.execute(sql)
print(res)

# 3、获取查询结果
# fetchall：获取查询集中所有内容
# res = cur.fetchall()
# print(res)

# fetchone()获取查询集的第一条数据
result = cur.fetchone()
print(result)

# 关闭游标
cur.close()
# 断开连接
con.close()
