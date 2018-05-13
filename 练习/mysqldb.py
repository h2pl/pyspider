#coding=utf-8
import MySQLdb
import random

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', 'root', '1234', 'wenda', charset='utf8')

    try:
        cursor = db.cursor()

        '''
        sql = 'insert into question(title, content, user_id, created_date, comment_count) values("xxx", "xxx", 1, now(), 0)'
        cursor.execute(sql)
        qid = cursor.lastrowid;

        #commit才是真正入库
        db.commit()
        print(qid)
        '''

        sql = 'select * from question order by id desc limit 2'
        cursor.execute(sql)

        #每行
        for each in cursor.fetchall():
            print(each)
            #每列
            for col in each:
                print(col)

    except Exception, e:
        print(e)
        db.rollback()
    db.close()