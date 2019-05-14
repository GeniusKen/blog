import pymysql
from utils import log


class myMysql(object):
    def __init__(self,
                 host,
                 port,
                 db,
                 user,
                 passwd,
                 charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    db=self.db,
                                    user=self.user,
                                    passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)

        return result


    def get_all(self, sql, params=()):
        list = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count

    fields = [
        'id',
        'created_time',
        'updated_time',
    ]

    @classmethod
    def get(cls, id):
        name = cls.__name__
        sql = """SELECT * FROM {} where id='{}'""".format(name,id)
        result = mysqlHelper.get_one(sql)
        return result


    @classmethod
    def new(cls,form={}):
        name = cls.__name__
        new_fields = []
        params = []
        for k,v in form.items():
            if k == 'desc':
                k = '`desc`'
            new_fields.append(k)
            params.append(v)
        sql = """insert into {name}({new_fields})values({mark})""".format(name = name ,new_fields = ','.join(new_fields),mark = ','.join(['%s']*len(new_fields)))
        mysqlHelper.insert(sql, params)
        get_sql = """SELECT * FROM {} where {}='{}'""".format(name, new_fields[0], params[0])
        all = mysqlHelper.get_all(get_sql)[0]
        return all


    @classmethod
    def all(cls):
        name = cls.__name__
        sql = 'SELECT * FROM {}'.format(name)
        all = list(mysqlHelper.get_all(sql))
        return all

    @classmethod
    def find_all(cls, **kwargs):
        name = cls.__name__
        k, v = '', ''
        for key, value in kwargs.items():
            k, v = key, value
        sql = """SELECT * FROM {} where {}='{}'""".format(name,k,v)
        all = list(mysqlHelper.get_all(sql))
        return all


mysqlHelper=myMysql('localhost',3306,'myBlog','root','mysql')


#创建category表
def create_category():
    mysqlHelper.connect()
    ct_sql = """CREATE TABLE CATEGORY (
             id int auto_increment primary key ,
             title  CHAR(20) not null,
             created_time INT default 1,  
             updated_time INT default 1 
             )"""
    mysqlHelper.cursor.execute("DROP TABLE IF EXISTS CATEGORY")
    mysqlHelper.cursor.execute(ct_sql)
    mysqlHelper.conn.commit()
    mysqlHelper.close()


#创建page表
def create_page():
    mysqlHelper.connect()
    ct_sql = """CREATE TABLE Page (
                 id int auto_increment primary key ,
                 title  CHAR(20) not null,
                 content char not null,
                 `desc` char(100) not null,
                 author char(20) not null,
                 category char(20) not null,
                 created_time INT default 1,  
                 updated_time INT default 1 
                 )"""
    mysqlHelper.cursor.execute("DROP TABLE IF EXISTS Page")
    mysqlHelper.cursor.execute(ct_sql)
    mysqlHelper.conn.commit()
    mysqlHelper.close()


#插入测试
def inser_test():
    mysqlHelper.connect()
    sql = """INSERT INTO Page(id,title,author,`desc`,category,created_time, content,updated_time)VALUES (1, '时光','时光','时光','时光', 1,'hhhh', 1)"""
    mysqlHelper.cursor.execute(sql)
    mysqlHelper.conn.commit()
    mysqlHelper.close()











