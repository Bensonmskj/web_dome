import pymysql

#执行查询sql，返回list of dict
#打开数据库连接
# db = pymysql.connect(
#     host = '49.235.92.12',
#     user = 'root',
#     password = '123456',
#     port = 3309,
#     db = 'online',
#     cursorclass=pymysql.cursors.DictCursor
# )
# #使用cursors创建游标对象
# cur = db.cursor()
# #使用execute()方法执行sql语句
# cur.execute('SELECT * from users_userprofile where username="1234@qq.com";')
# #使用fetchall()方法获取查询结果
# result = cur.fetchall()
# print("查询的结果为：",result)#返回list of dict
# #关闭数据库连接
# db.close()

#配置数据库相关信息
dbinfo = {
    "host":"49.235.92.12",
    "user":"root",
    "password":"123456",
    "port":3309}

class DbConnect():
    def __init__(self,db_conf,database=""):
        try:
            self.db_conf = db_conf
            #打开数据库连接
            self.db = pymysql.connect(
                database=database,
                cursorclass=pymysql.cursors.DictCursor,
                **db_conf)
            #激活游标
            self.curses = self.db.cursor()
        except Exception as e:
            print("连接失败%s" % e)

    def select(self,sql):
        try:
            self.curses.execute(sql)
            resutl = self.curses.fetchall()
            print("获取到的结果为：",resutl)
            print(resutl[0]["username"])
            return resutl
        except Exception as e:
            print("查询失败：%s"%e)

    def execute(self,sql):
        try:
            self.curses.execute(sql)
            self.db.commit()
        except Exception as e:
            print("操作失败：%s" % e)
            #发生错误时回滚
            self.db.rollback()

    def close(self):
        self.curses.close()

if __name__=='__main__':
    db = DbConnect(dbinfo,"online")
    sql1 = 'SELECT * from users_userprofile where username="1234@qq.com";'
    db.select(sql1)
    sql2 = 'DELETE FROM users_userprofile WHERE username = "0@qq.com";'
    db.execute(sql2)
    db.close()


