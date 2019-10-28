# -*-coding: utf-8-*-
import pyodbc


def access_handle(db_path=''):
    """
    连接Microsoft的Access数据表
    :param db_path: Access数据表的所在路径
    :return:
    """
    # 连接.mdb或者.accdb文件 (连接.accdb文件需要下载"ACE"驱动程序)
    # cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % (db_path,))

    # 连接.mdb文件
    cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (db_path,))
    # 创建一个游标对象
    crsr = cnxn.cursor()
    print('Connect --> {} successful'.format(db_path))

    # 打印数据库goods.mdb中的所有表的表名
    for table_info in crsr.tables(tableType='TABLE'):
        print('Found table name: {}'.format(table_info.table_name))

    # 创建新表 users
    crsr.execute('CREATE TABLE users (login VARCHAR(8), userid INT, projid INT)')
    # 给表中插入新数据
    crsr.execute("INSERT INTO users VALUES('Linda', 211, 151)")
    # 更新数据
    crsr.execute("UPDATE users SET projid=1 WHERE userid=211")
    print(crsr.rowcount)  # 想知道数据被修改和删除时，到底影响了多少条记录，这个时候你可以使用cursor.rowcount的返回值

    # 查询表格内所有数据
    for row in crsr.execute("SELECT * from users"):
        print(row)

    # 删除行数据
    # crsr.execute("DELETE FROM users WHERE login='Linda'")

    # 删除表users
    # crsr.execute("DROP TABLE users")

    # 提交数据（只有提交之后，所有的操作才会对实际的物理表格产生影响）
    crsr.commit()
    crsr.close()
    cnxn.close()


if __name__ == '__main__':
    access_handle(db_path=r'C:\Users\evaliu\Desktop\test.mdb')
