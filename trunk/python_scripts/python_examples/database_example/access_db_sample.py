# -*- coding:utf-8 -*-
import pyodbc


def access_table_read(db_path):
    """
    连接Microsoft的Access数据表读取数据
    :param db_path: Access数据表的所在路径
    :return:
    """
    # 连接.mdb或者.accdb文件 (连接.accdb文件需要下载"ACE"驱动程序)
    # cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s' % db_path)

    # 连接.mdb文件
    cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % db_path)
    # 获取一个句柄
    crsr = cnxn.cursor()

    # 创建表users
    crsr.execute("CREATE TABLE users (login VARCHAR(8), id INT, age INT)")
    # 插入数据到users表
    crsr.execute("INSERT INTO users VALUES('Linda', 66, 20)")
    # 更新users表中数据
    crsr.execute("UPDATE users SET age=22 WHERE login='Linda' and id=66")  # 多条件选择用and
    print(crsr.rowcount)  # 查看更新状态
    # 查询users表中数据
    print([i for i in crsr.execute("SELECT * from users")])  # 查询所有数据
    print([i for i in crsr.execute("SELECT * from users WHERE login='Linda'")])  # 查询指定数据
    # 查询数据库中的所有表名
    print([i.name for i in crsr.tables(tableType='TABLE')])
    # 删除users表中数据
    crsr.execute("DELETE FROM users WHERE login='Linda'")
    # 删除表users
    crsr.execute("DROP TABLE users")

    # 提交数据（只有提交之后，所有的操作才会生效）
    crsr.commit()
    # 关闭句柄
    crsr.close()
    cnxn.close()


if __name__ == '__main__':
    access_table_read(db_path=r'C:\Users\evaliu\Desktop\test.mdb')
