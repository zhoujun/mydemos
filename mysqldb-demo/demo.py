#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","","db_demo" )

def test_create_table():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute("DROP TABLE IF EXISTS employee")

    # 创建数据表SQL语句
    sql = """CREATE TABLE employee (
             name  varchar(20) NOT NULL,
             age int,
             sex char(1)
             )"""

    cursor.execute(sql)

def test_insert():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO employee (name, age, sex)
             VALUES ('Mac',  20, 'M')"""
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # 关闭数据库连接
    db.close()

def test_select():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("select * from employee")

    # 使用 fetchone() 方法获取一条数据库。
    data = cursor.fetchone()
    print "data: ", data

    # 关闭数据库连接
    db.close()



if __name__ == '__main__':
    # test_create_table()
    # test_insert();
    test_select()
