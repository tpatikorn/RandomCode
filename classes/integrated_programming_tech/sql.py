import pymysql


def db_connect():
    try:
        _conn = pymysql.connect(user='rmutsb_icp', password='rmutsb_icp',
                                host='db4free.net', port=3306,
                                database='rmutsb_icp', charset='utf8')
        _cur = _conn.cursor()
        _cur.execute("create table students (id integer, name string")
        return _conn, _cur
    except pymysql.Error:
        print("Error User ,Password Or Database is not correct")

db_connect()

