import pymysql


class HandleDB:

    def __init__(self, host, port, user, password, *args, **kwargs):
        self.con = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=password,
                                   charset='utf8',
                                   # cursorclass=pymysql.cursors.DictCursor
                                   *args, **kwargs
                                   )

    def find_one(self, sql):
        """查询一条数据"""
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def find_all(self, sql):
        """查询所有数据"""
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def find_count(self, sql):
        """sql执行完之后，返回数据条数"""
        cur = self.con.cursor()
        res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()


if __name__ == '__main__':
    from common.handle_conf import conf

    sql = "select * from futureloan.member where id < 5"
    db = HandleDB(
        host=conf.get("mysql", "host"),
        port=conf.getint("mysql", "port"),
        user=conf.get("mysql", "user"),
        password=conf.get("mysql", "password")
    )
    res = db.find_one(sql)
    print(res)
