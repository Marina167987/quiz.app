import sqlite3
 
con = sqlite3.connect("quiz.db")
cursor = con.cursor() 

def load_question(con):
    print("Введите текст вопроса")
    text_question = input()
    print("ВЫберите вариант ответа")
    options = input()
    print("Введите правильный ответ на вопрос")
    answers = int(input())
    print("Введите уровень сложности")
    difficulty_level = int(input())
    cur = con.cursor()
    cur.execute("INSERT INTO questions (text_questions, options, answers, difficulty_level) VALUES (?, ?, ?, ?)", 
                (text_question, options, answers, difficulty_level))
    con.commit()
    cursor.execute("SELECT * FROM questions")
    print(cursor.fetchall())


load_question(con)