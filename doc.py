# -*- coding: UTF-8 -*-
import pymysql
import pymysql.cursors

def insertType(environ):
  connection = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               db='doc',
                               port=3306,
                               charset='utf8')
  try:
    with connection.cursor() as cursor:
      # cursor.execute('insert into intl (name) values (%s)', ['中文'])
      # print(cursor.lastrowid)
      cursor.execute('SELECT * FROM intl')
      connection.commit()
      return cursor.fetchall()
  finally:
    connection.close()

