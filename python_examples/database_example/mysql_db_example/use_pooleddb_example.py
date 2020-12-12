import MySQLdb
from DBUtils.PooledDB import PooledDB


class MysqlHandle(object):

    def __init__(self, host='10.167.219.250', port=3306, user='npbg', password='', db_name='npbg'):
        """
        数据库连接池初始化
        :param host: 数据库地址
        :param port: 数据库端口
        :param user: 用户名
        :param password: 登陆密码
        :param db_name: 数据库名
        """
        self.pool = PooledDB(
            creator=MySQLdb,
            mincached=0,
            maxcached=6,
            maxshared=3,
            blocking=True,
            ping=0,
            maxusage=None,
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port,
            charset='utf8mb4'
        )

    def execute_sql_command(self, sql='', as_dict=True):
        """
        执行SQL命令，如果是SELECT返回查询结果，如果不是，执行并commit
        :param sql: Mysql语句
        :param as_dict: 是否将结果转换为字典类型
        :return:
        """
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()  # 使用池子连接数据库
            cursor = conn.cursor(MySQLdb.cursors.DictCursor) if as_dict else conn.cursor()
            cursor.execute(sql)
            if 'SELECT' in sql.upper():
                return cursor.fetchall()
            else:
                conn.commit()
                return True
        except Exception as ex:
            print('SQL: [{}] execute failed, error msg: {}'.format(sql, ex))
            if 'SELECT' in sql.upper():
                return ()
            conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
