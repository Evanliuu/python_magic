import MySQLdb
from DBUtils.PooledDB import PooledDB


class MysqlHandle(object):

    def __init__(self, host='10.167.219.250', port=3306, user='npbg', password='', db_name='npbg'):
        """
        ���ݿ����ӳس�ʼ��
        :param host: ���ݿ��ַ
        :param port: ���ݿ�˿�
        :param user: �û���
        :param password: ��½����
        :param db_name: ���ݿ���
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
        ִ��SQL��������SELECT���ز�ѯ�����������ǣ�ִ�в�commit
        :param sql: Mysql���
        :param as_dict: �Ƿ񽫽��ת��Ϊ�ֵ�����
        :return:
        """
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()  # ʹ�ó����������ݿ�
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
