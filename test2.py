import pymysql
from pymysql.cursors import DictCursor

# host=None, user=None, password="", database=None, port=0
conn = None
cursor = None
try:  # 连接处理
    conn = pymysql.connect('192.168.243.145', 'root', '123456', 'school')  # print(conn.ping(False))
    # cursor = conn.cursor()  # default
    cursor = conn.cursor(cursor=DictCursor)
    # try:  # 事物处理
    #     for i in range(10):
    #         name = 'tom'
    #         age = 20
    #         insert_sql = "insert into student (name, age) values ('{0}{2}', {1})".format(name, age, i)
    #         rows = cursor.execute(insert_sql)
    #     conn.commit()
    # except Exception as e:
    #     print(e)
    #     conn.rollback()
    # #  一个连接内可以有多个事物
    print('-------------')
    cursor.execute("insert into student (name, age) values ('add', 100)")

    sel_seq = "select * from student where name like %(name)s and age > %(age)s"

    # userid = '6 or 1=1'
    # sel_seq = "select * from student where id = %s "

    line_count = cursor.execute(sel_seq, args={'name': '%', 'age': 10})  # -> int
    print(cursor.fetchall())  # 虽然没有提交但是自己可以看到改变,真正的落地要提交才行
    print('-------------')

    print(cursor.rowcount)
    print(cursor.rownumber)

    print(cursor.fetchone())

    print(cursor.rowcount)
    print(cursor.rownumber)

    print(cursor.fetchone())

    print(cursor.rowcount)
    print(cursor.rownumber)
    # print(cursor.fetchmany(100))

    print(cursor.fetchall())

    print(cursor.rowcount)
    print(cursor.rownumber)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    # print(conn.ping(False))
