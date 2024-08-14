import sqlite3

def get_user_info(user_id):
    # 데이터베이스 연결
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    # SQL Injection 취약점이 있는 쿼리
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

# 사용자 입력 시뮬레이션
user_input = input("Enter user ID: ")
user_info = get_user_info(user_input)
print(user_info)
