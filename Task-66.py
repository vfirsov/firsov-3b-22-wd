# Создайте базу данных для хранения информации о студентах, включающую их имена, возвраст, средний балл.
# Затем выведите все данные на экран
import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXIST students
                        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, avg_score REAL)''')


def insert_students():
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Маслов Артём Александрович", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Смирнов Артемий Лукич", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Верещагина Варвара Ивановна", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Устинов Михаил Артёмович", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Алексеева Валерия Леоновна", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Зорин Фёдор Артёмович", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Иванов Георгий Матвеевич", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Сорокина Есения Павловна", 20, 5))
    cursor.execute("INSERT INTO students (name, age, avg_score) VALUES (?, ?, ?)", ("Демьянов Кирилл Ярославович", 20, 5))


# Столкнулся с проблемой повторного добавления данных в таблицу
