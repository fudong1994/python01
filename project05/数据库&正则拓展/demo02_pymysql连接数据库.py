import pymysql

# 1、连接数据库
con = pymysql.connect(host='api.lemonban.com',
                      port=3306,
                      user='future',
                      password="123456",
                      charset='utf8')

# 2、创建游标对象
cur = con.cursor()

sql = ''
# 3、执行sql语句
cur.execute(sql)

# 提交事务（增删改时需提交事务）
con.commit()

cur.close()
con.close()
