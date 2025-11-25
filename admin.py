import sqlite3

def load_question(text_question, options, answers, difficulty_level):
    con = sqlite3.connect("quiz.db")
    
    cur = con.cursor()
    
    # Создаем таблицу questions, если она не существует
    cur.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_questions TEXT NOT NULL,
            options TEXT NOT NULL,
            answers INTEGER NOT NULL,
            difficulty_level INTEGER NOT NULL
        )
    ''')
    
    cur.execute("INSERT INTO questions (text_questions, options, answers, difficulty_level) VALUES (?, ?, ?, ?)", 
                (text_question, options, answers, difficulty_level))
    con.commit()
    
    cur.execute("SELECT * FROM questions")
    print("Все вопросы в базе:")
    for row in cur.fetchall():
        print(row)

    con.close()
