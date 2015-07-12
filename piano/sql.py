#!/usr/bin/python

import sqlite3

# 通用的执行sql函数
def sql_ez(sql):
    conn = sqlite3.connect('test.db')
    print "Opened database successfully";
    conn.ezecute(sql)
    print "Table created successfully";
    conn.close()

# 建表语句

#评论表
CREATE_TABLE_COMMENT =
'''
CREATE TABLE COMMENT
(
COMMENTID INT PRIMARY KEY NOT NULL;
USERID INT NOT NULL;
PIANOID INT NOT NULL;
COMMENTContent CHAR(200);
)
'''
# 收藏表
CREATE_TABLE_COLLECTION =
'''
CREATE TABLE COLLECTION
(
COLLECTIONID INT PRIMARY KEY NOT NULL;
USERID INT NOT NULL,
PIANOID INT NOT NULL,
CollectorName CHAR(20) NOT NULL;
)
'''
# 用户表
CREATE_TABLE_USER =
'''
CREATE TABLE USER
(
USERID INT PRIMARY KEY NOT NULL,
USERName CHAR(20) NOT NULL,
Email CHAR(50) NOT NULL,
Password CHAR(30) NOT NULL,
)
'''

#钢琴表

CREATE_TABLE_PIANO =
'''
CREATE TABLE PIANO
(
PIANOID INT PRIMARY KEY NOT NULL,
USERID INT NOT NULL,
Title CHAR(20) NOT NULL,
Brand CHAR(20) NOT NULL,
Price CHAR(10) NOT NULL,
UseTime CHAR(20) NOT NULL,
ImgLink CHAR(20) NOT NULL,
Information CHAR(200),
)
'''


def create_table():
    sql_ez(CREATE_TABLE_USER)
    sql_ez(CREATE_TABLE_PIANO)
    sql_ez(CREATE_TABLE_COMMENT)
    sql_ez(CREATE_TABLE_COLLECTION)

#
# 登陆
# 用户表根据邮箱查询用户密码
# 修改密码页面
# 用户表根据当前用户的邮箱查询密码
def get_password(email):
    return sql_ez('select Password from USER where Email = ' + email)


# 发布钢琴页面
# 钢琴表插入一个钢琴信息
def add_piano(PIANOID , USERID , Title , Brand , Price , UseTime , ImgLink , Information):
    return sql_ez('insert into PIANO values( ' + PIANOID ,USERID , Title , Brand , Price , UseTime , ImgLink , Information +')')

# 在钢琴表查询钢琴id（y）为z的钢琴的所有信息
def get_infomation(z):
    return sql_ez('select* from PIANO where PIANOID = '+ z)

# 在评论表查询钢琴id为z（y）的所有评论
def get_COMMENT(piano_id):
    return sql_ez('select* from COMMENT where PIANOID = 'piano_id )

# 注册
# 用户表插入一个用户
def add_USER(USERID , USERName , Email , Password):
    return  sql_ez('insert into USER values( ' + USERID , USERName , Email , Password + ' )')

# 主页
# 在钢琴表查询所有钢琴所有信息
def get_pianos():
    return sql_ez('select* from PIANO')

# 单个钢琴页面
def get_piano(id):
    return sql_ez('select* from PIANO where PIANOID = ' + id)



# 在评论表插入一条新的评论（y）
def add_COMMENT(COMMENTID , USERID,PIANOID , COMMENTCotent):
    return sql_ez('insert into COMMENT values(' + COMMENTID , USERID,PIANOID , COMMENTCotent + ')')


# 收藏页面
# 收藏表查询当前用户的邮箱（y）的所有收藏的钢琴的信息
def get_piano(USERID, email):
    return sql_ez('select* from COLLECTION,USER where Collction.USERID = ' + USERID + 'AND Email = ' + email)
