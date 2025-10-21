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
cursor.execute('''
                INSERT INTO users (id,name,age,email)
                values (3,'박지훈',28,'candoit_8521@naver.com');
               ''')
print('테이블 생성 완료')
# 저장
conn.commit()
# 닫아주기
conn.close()