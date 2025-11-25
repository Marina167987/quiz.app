import tkinter as tk
from database import registration
import sqlite3
from tkinter.messagebox import showinfo 

root = tk.Tk()     # создаем корневой объект - окно
root.title("QuizApp")     # устанавливаем заголовок окна
root.geometry("1000x800")    # устанавливаем размеры окна
root.configure(bg='white')
root.resizable(False, False) # заблокировать расширение окна

def start_quiz():
    """Функция, которая вызывается при нажатии кнопки 'Начать'"""
    first_name = entry_name.get()
    last_name = entry_surname.get()
    grade = entry_class.get()
    age = entry_age.get()
    
    # МОЖНО ДОБАВИТЬ - проверка, что все поля заполнены 
    if first_name and last_name and grade and age:
        try:
            age = int(age)  # преобразуем возраст в число
            id = registration(first_name, last_name, age, grade)
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

    registration_label = tk.Label(root, text="Регистрация", font=("Arial", 16, "bold"), bg="#71ddcb",fg='#333')
    registration_label.pack(pady=15)

    label_name = tk.Label(root, text="Введите имя", font=("Arial", 14),  bg="white",fg='#333')
    label_name.pack(padx = 30, pady = 15, anchor="w")
    
    entry_name = tk.Entry(root)
    entry_name.pack(padx=30, pady=15, anchor="w")

    label_surname = tk.Label(root, text="Введите фамилию", font=("Arial", 14),  bg="white",fg='#333')
    label_surname.pack(padx = 30, pady = 15, anchor="w")
    
    entry_surname = tk.Entry(root)
    entry_surname.pack(padx=30, pady=15, anchor="w")

    label_class = tk.Label(root, text="Введите класс", font=("Arial", 14),  bg="white",fg='#333')
    label_class.pack(padx = 30, pady = 15, anchor="w")
    
    entry_class = tk.Entry(root)
    entry_class.pack(padx=30, pady=15, anchor="w")

    label_age = tk.Label(root, text="Введите возраст", font=("Arial", 14),  bg="white",fg='#333')
    label_age.pack(padx = 30, pady = 15, anchor="w")
    
    entry_age = tk.Entry(root)
    entry_age.pack(padx=30, pady=15, anchor="w")

    #  ИСПРАВЛЕНО - вызов функции в command= без скобок 
    btn = tk.Button(root, text="Начать", command=start_quiz)
    btn.pack(padx=10, pady=20)
    
    # Возвращаем элементы ввода, если они понадобятся позже
    return entry_name, entry_surname, entry_class, entry_age

# Создаем виджеты и получаем ссылки на поля ввода
entry_name, entry_surname, entry_class, entry_age = create_widgets(root)

root.mainloop() # запуск приложения