import sqlite3

def registration(first_name, last_name, age, grade):
    con = sqlite3.connect("quiz.db")
    cursor = con.cursor()
    
    # Создаем таблицу students, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    
    cursor.execute("INSERT INTO students (first_name, last_name, age, grade) VALUES (?, ?, ?, ?)", 
                (first_name, last_name, age, grade))
    con.commit()
    
    cursor.execute("SELECT id FROM students WHERE first_name=? and last_name=?", (first_name, last_name))
    student_id = cursor.fetchone()
    print(student_id)
    con.close()
    return student_id # возвращаем id студента (число)
