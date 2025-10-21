import pymysql

# sql접속 객체 생성
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database ='exampledb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
cursor.execute("show tables")
print('현재 존재하는 테이블 : ',cursor.fetchall())
conn.close()