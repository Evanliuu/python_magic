# -*- coding:utf-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB

__author__ = 'Evan'


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
        执行SQL命令，如果是SELECT会返回所有的查询结果，通用方法
        :param sql: Mysql语句
        :param as_dict: 是否将结果转换为字典类型
        :return:
        """
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()  # 使用pool连接数据库
            cursor = conn.cursor(MySQLdb.cursors.DictCursor) if as_dict else conn.cursor()
            cursor.execute(sql)
            if 'SELECT' in sql.upper():
                return list(cursor.fetchall())
            else:
                conn.commit()
                return True
        except Exception as ex:
            print('SQL: [{}] execute failed, error msg: {}'.format(sql, ex))
            if 'SELECT' in sql.upper():
                return []
            conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def manipulate_data_table(self, data_table='', action='QUERY', **params):
        """
        对数据表进行增删改查，通用方法
        :param data_table: 数据表名
        :param action: 要执行的动作，'ADD' or 'UPDATE' or 'DELETE' or 'QUERY'
        :param params: 需要使用的参数，dict

        params example:
            if action == 'ADD':
                params = {
                    'fields': ['id', 'name', 'value'],
                    'values': ['1', 'Evan', '6']
                }
            elif action == 'UPDATE':
                params = {
                    'field': 'name',
                    'new_value': 'Evan',
                    'where': 'name="other"' or ''
                }
            elif action == 'DELETE':
                params = {
                    'where': 'name="Evan"'
                }
            else:
                params = {
                    'where': 'name="Evan"' or ''
                }
        :return:
        """
        if action == 'ADD':
            assert params.get('fields'), '缺少fields参数'
            assert params.get('values'), '缺少values参数'
            assert isinstance(params['fields'], list), 'fields必须是个列表'
            assert isinstance(params['values'], list), 'values必须是个列表'
            assert len(params['values']) == len(params['fields']), 'values长度必须和fields长度一致'

            # 拼接所有参数
            sql = """INSERT INTO {0}({1}) VALUES('{2}')""".format(data_table,
                                                                  ','.join(str(f) for f in params['fields']),
                                                                  '","'.join(str(v) for v in params['values']))
            self.execute_sql_command(sql)

        elif action == 'UPDATE':
            assert params.get('field'), '缺少fields参数'
            assert params.get('new_value'), '缺少new_value参数'

            if params.get('where'):  # 处理有WHERE的情况
                sql = """UPDATE {0} SET {1}='{2}' WHERE {3}""".format(data_table, params['field'],
                                                                      params['new_value'], params['where'])
            else:
                sql = """UPDATE {0} SET {1}='{2}'""".format(data_table, params['field'], params['new_value'])
            self.execute_sql_command(sql)

        elif action == 'DELETE':
            assert params.get('where'), '缺少where参数'
            sql = """DELETE FROM {0} WHERE {1}""".format(data_table, params['where'])
            self.execute_sql_command(sql)

        else:  # Default QUERY
            if params.get('where'):
                sql = """SELECT * FROM {0} WHERE {1}""".format(data_table, params['where'])
            else:
                sql = """SELECT * FROM {}""".format(data_table)

            data = self.execute_sql_command(sql)
            if data:
                return data
            else:
                return []


SQL = MysqlHandle()
