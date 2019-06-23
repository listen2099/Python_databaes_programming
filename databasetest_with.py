import pymysql
from pymysql.cursors import DictCursor

conn = None
try:  # 连接处理
    conn = pymysql.connect('192.168.243.145', 'root', '123456', 'school')  # print(conn.ping(False))
    # cursor = conn.cursor()  # default
    with conn as cursor:
    # cursor = conn.cursor(cursor=DictCursor)
        with cursor:
            userid = "tom"
            sel_seq = "select * from student where name = %s "
            line_count = cursor.execute(sel_seq, args={'name': 'tom%', 'age': 10})  # -> int
finally:
    if conn:
        conn.close()
