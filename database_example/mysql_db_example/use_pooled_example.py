"""
使用PooledDB连接池连接Mysql数据库
"""
# -*- coding:utf-8 -*-
import pymysql
from DBUtils.PooledDB import PooledDB

__author__ = 'Evan'


class MysqlHandle(object):

    def __init__(self, host='localhost', user='root', password='', db_name='', port=3306):
        """
        初始化PooledDB连接池
        :param host: 数据库地址
        :param port: 数据库端口
        :param user: 用户名
        :param password: 登陆密码
        :param db_name: 数据库名
        """
        self.pool = PooledDB(
            creator=pymysql,
            mincached=0,  # 连接池中空闲连接的初始数量
            maxcached=6,  # 连接池中空闲连接的最大数量
            maxshared=3,  # 共享连接的最大数量
            maxconnections=0,  # 连接池最大值，默认无上限
            blocking=True,  # 超过最大连接数的处理，为True阻塞连接，等待连接池空位，为False直接报错
            ping=0,
            maxusage=None,  # 单个连接的最大重复使用次数，默认无限制
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=port,
            charset='utf8mb4'
        )

    def execute_sql(self, sql, as_dict=True):
        """
        执行SQL命令，如果是SELECT会返回所有的查询结果，通用方法
        :param sql: SQL语句
        :param as_dict: 是否将结果转换为字典类型，默认True
        :return:
        """
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()  # 使用pool连接数据库
            cursor = conn.cursor(pymysql.cursors.DictCursor) if as_dict else conn.cursor()
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
            if conn:
                conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def execute_many_sql(self, sql, params):
        """
        同时执行多次SQL命令
        :param sql: SQL语句，例：'INSERT INTO table (id,name) VALUES (%s,%s)'  # 占位符统一使用 %s，且不能加上引号
        :param params: 必须是元组或列表类型，例：((), ()) or [(), ()]
        :return:
        """
        conn = None
        cursor = None
        try:
            conn = self.pool.connection()  # 使用pool连接数据库
            cursor = conn.cursor()
            cursor.executemany(sql, params)
            conn.commit()
            return True
        except Exception as ex:
            print('SQL: [{}] execute failed, error msg: {}'.format(sql, ex))
            if conn:
                conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def manipulate_data_table(self, data_table, action='QUERY', **params):
        """
        对数据表进行增删改查，通用方法
        :param data_table: 数据表名
        :param action: 要执行的事务，'ADD' or 'UPDATE' or 'DELETE' or 'QUERY'
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
            else:  # Default QUERY
                params = {
                    'fields': ['id', 'name', 'value'] or ''
                    'where': 'name="Evan"' or ''
                }
        :return:
        """
        assert data_table, '缺少data_table参数'
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

        elif action == 'UPDATE':
            assert params.get('field'), '缺少fields参数'
            assert params.get('new_value'), '缺少new_value参数'
            if params.get('where'):  # 处理有WHERE的情况
                sql = """UPDATE {0} SET {1}='{2}' WHERE {3}""".format(data_table, params['field'],
                                                                      params['new_value'], params['where'])
            else:
                sql = """UPDATE {0} SET {1}='{2}'""".format(data_table, params['field'], params['new_value'])

        elif action == 'DELETE':
            assert params.get('where'), '缺少where参数'
            sql = """DELETE FROM {0} WHERE {1}""".format(data_table, params['where'])

        else:  # Default QUERY
            if params.get('fields'):  # 如果fields有值，返回指定的field values
                assert isinstance(params['fields'], list), 'fields必须是个列表'
                fields = ','.join(str(f) for f in params['fields'])

                if params.get('where'):  # 处理有WHERE的情况
                    sql = """SELECT {0} FROM {1} WHERE {2}""".format(fields, data_table, params['where'])
                else:
                    sql = """SELECT {0} FROM {1}""".format(fields, data_table)
            else:  # 返回所有字段
                if params.get('where'):
                    sql = """SELECT * FROM {0} WHERE {1}""".format(data_table, params['where'])
                else:
                    sql = """SELECT * FROM {}""".format(data_table)

        return self.execute_sql(sql)


SQL = MysqlHandle()
