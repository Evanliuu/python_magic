# -*- coding:utf-8 -*-
import sqlite3

__author__ = 'Evan'


class SqliteDB(object):
    """
    在本地创建一个虚拟的sql文件
    """
    def __init__(self, db_path=r'C:\Users\evaliu\Desktop', db_name='sql_lite3'):
        self.db_path = db_path + '\\' + db_name
        # 创建一个虚拟的Mysql文件
        self.cxn = sqlite3.connect(self.db_path)
        self.cur = self.cxn.cursor()

    def create_table(self):
        """
        创建一个数据表
        :return:
        """
        try:
            self.cur.execute('''
            CREATE TABLE users(
                uid INTEGER,
                prid INTEGER)
            ''')
        except Exception as e:
            print('Create Table Error, ERROR-MSG: [ {} ]'.format(e))
            print('Recreate the users now!')
            self.cur.execute('DROP TABLE users')
            self.create_table()

    def read_table(self):
        """
        读取数据表
        :return:
        """
        print('Mysql dumps:')
        self.cur.execute('SELECT * FROM users')
        for each_line in self.cur.fetchall():
            print(each_line)


if __name__ == '__main__':
    mysql = SqliteDB()
    try:
        mysql.create_table()
        mysql.cur.execute('INSERT INTO users VALUES(100, 200)')
        mysql.read_table()
    finally:
        mysql.cur.close()
        mysql.cxn.commit()
        mysql.cxn.close()
