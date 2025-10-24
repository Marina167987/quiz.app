import sqlite3
 
con = sqlite3.connect("quiz.db")
cursor = con.cursor()
 
# создаем таблицу students
#cursor.execute("""CREATE TABLE students
 #               (id INTEGER PRIMARY KEY AUTOINCREMENT,  
  #              first_name TEXT,
   #             last_name TEXT,
    #            age INTEGER,
     #           grade TEXT)
      #      """)


cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("SELECT first_name, last_name FROM students")
print(cursor.fetchall())

cursor.execute("SELECT COUNT(*) FROM students")
print(f"Количество учеников в б/д: {cursor.fetchone()[0]}")