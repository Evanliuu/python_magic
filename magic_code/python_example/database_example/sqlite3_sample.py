import sqlite3


class Mysql(object):
    """
    不需要连接真实的Mysql数据库，在本地创建一个虚拟的Mysql文件
    """
    def __init__(self, db_path=r'C:\pycharm_user\evan', db_name='sql_lite3'):
        self.db_name = db_name
        self.db_path = db_path + '/' + self.db_name
        # connect virtual Mysql database
        self.cxn, self.cur = self._connect()

    def _connect(self):
        self.cxn = sqlite3.connect(self.db_path)
        self.cur = self.cxn.cursor()
        return self.cxn, self.cur

    def create_table(self):
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
        print('Mysql dump:')
        self.cur.execute('SELECT * FROM users')
        for each_line in self.cur.fetchall():
            print(each_line)


if __name__ == '__main__':
    mysql = Mysql()
    try:
        mysql.create_table()
        mysql.cur.execute('INSERT INTO users VALUES(100, 200)')
        mysql.read_table()
    finally:
        mysql.cur.close()
        mysql.cxn.commit()
        mysql.cxn.close()
