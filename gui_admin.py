import tkinter as tk
from database import registration
import sqlite3
from tkinter.messagebox import showinfo 
from admin import load_question

root = tk.Tk()     # создаем корневой объект - окно
root.title("QuizApp")     # устанавливаем заголовок окна
root.geometry("1200x1000")    # устанавливаем размеры окна
root.configure(bg='white')
root.resizable(False, False) # заблокировать расширение окна

def start_quiz():
    """Функция, которая вызывается при нажатии кнопки 'Начать'"""
    text_question = entry_text_question.get()
    options = entry_surname.get()
    answers = entry_class.get()
    difficulty_level = entry_difficulty_level.get()
    
    # МОЖНО ДОБАВИТЬ - проверка, что все поля заполнены 
    if text_question and options and answers and difficulty_level:
        try:
            answers = int(answers)  # преобразуем возраст в число
            load_question(text_question, options, answers, difficulty_level)
            # Здесь можно добавить переход к следующему окну с вопросами
            print(f"Пользователь {first_name} {last_name} зарегистрирован с ID{id}!")
            if id is not None:
                showinfo(title="Информация", message="Успешная регистрация")
        except ValueError:
            print("Возраст должен быть числом!")
    else:
        print("Заполните все поля!")

def create_widgets(root):
    title_label = tk.Label(root, text="Викторина по основам Python", font=("Arial", 16, "bold"), bg="#71ddcb",fg='#333')
    title_label.pack(padx=10, pady=20)

    add_question_label = tk.Label(root, text="Добавление вопросов", font=("Arial", 16, "bold"), bg="#71ddcb",fg='#333')
    add_question_label.pack(pady=15)

    label_text_question = tk.Label(root, text="Введите текст вопроса", font=("Arial", 14),  bg="white",fg='#333')
    label_text_question.pack(padx = 30, pady = 15, anchor="w")
    
    entry_text_question = tk.Text(root, height=3, font=("Arial", 16), width=50, wrap="word", borderwidth=2.0)
    entry_text_question.pack(padx=30, pady=15, anchor="w")

    label_options = tk.Label(root, text="Введите варианты ответов", font=("Arial", 14),  bg="white",fg='#333')
    label_options.pack(padx = 30, pady = 15, anchor="w")
    
    entry_options = tk.Text(root, height=3, font=("Arial", 16), width=50, wrap="word", borderwidth=2.0)
    entry_options.pack(padx=30, pady=15, anchor="w")

    label_answer = tk.Label(root, text="Введите вариант правильного ответа", font=("Arial", 14),  bg="white",fg='#333')
    label_answer.pack(padx = 30, pady = 15, anchor="w")
    
    entry_answer = tk.Text(root, height=3, font=("Arial", 16), width=50, wrap="word", borderwidth=2.0)
    entry_answer.pack(padx=30, pady=15, anchor="w")

    label_difficulty_level = tk.Label(root, text="Введите уровень сложности", font=("Arial", 14),  bg="white",fg='#333')
    label_difficulty_level.pack(padx = 30, pady = 15, anchor="w")
    
    entry_difficulty_level = tk.Text(root, height=3, font=("Arial", 16), width=50, wrap="word", borderwidth=2.0)
    entry_difficulty_level.pack(padx=30, pady=15, anchor="w")

    #  ИСПРАВЛЕНО - вызов функции в command= без скобок 
    btn = tk.Button(root, text="Начать", command=start_quiz)
    btn.pack(padx=10, pady=20)
    
    # Возвращаем элементы ввода, если они понадобятся позже
    return entry_text_question, entry_options, entry_answer, entry_difficulty_level

# Создаем виджеты и получаем ссылки на поля ввода
entry_name, entry_surname, entry_class, entry_age = create_widgets(root)

root.mainloop() # запуск приложения