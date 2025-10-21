import pymysql

# 데이터베이스와 연결
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'exampledb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

#명령어 입력기 선택 
cursor = conn.cursor()
# 명령어 실행
cursor.execute("DELETE FROM users where id = 3")
# 저장
conn.commit()
# 닫아주기
conn.close()