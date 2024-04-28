import sqlite3

""" 
Чтобы подключиться к БД, используем метод connect: 
"""
# conn = sqlite3.connect('database.db')
# # some code here
# conn.close()

""" 
Лучше предпочесть контекстный менеджер 
для корректного завершения работы в случае возникновения ошибок. 
"""
# with sqlite3.connect('database.db') as conn:
#     # some code here

""" 
Чтобы использовать SQL и получать результаты запросов, нужен курсор. 
Это специальный объект, создаваемый методом cursor().
Метод .execute исполняет переданный SQL-запрос. 
С помощью fetchall() мы можем получить все записи, 
который этот запрос нам вернул, в виде списка кортежей.
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM students;')
#     print(cursor.fetchall())

"""
Создание таблицы
Наша таблица будет называться students, в ней мы будем хранить информацию о студентах — их id, имена и фамилии.
sqlite> CREATE TABLE students(
   ...>   id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>   name TEXT NOT NULL,
   ...>   surname TEXT NOT NULL
   ...> );
INTEGER — целочисленный тип данных.
TEXT — строковый тип данных.
NOT NULL означает, что поле не может быть пустым.
PRIMARY KEY говорит, что этот ключ будет первичным, — его значения будут уникальными для всей таблицы.
AUTOINCREMENT означает, что при создании нового студента его id будет увеличен на 1 относительно последнего.

Важно! После добавления, изменения или удаления записей 
необходимо внести изменения с помощью метода commit у объекта Connection:
conn.commit()
Иначе они не зафиксируются в базе.
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute(
#         'CREATE TABLE students'
#         '('
#         'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#         'name TEXT NOT NULL, '
#         'surname TEXT NOT NULL'
#         ');'
#     )
#     conn.commit()

"""
Создание записи
Для создания записи мы используем оператор INSERT:
sqlite> INSERT INTO students (name, surname) VALUES ('Иван', 'Иванов');
sqlite> INSERT INTO students (name, surname) VALUES ('Петр', 'Петров');
sqlite> INSERT INTO students (name, surname) VALUES ('Анна', 'Аннова');
В первых скобках указываются поля, которые мы добавляем; в соответствии с ними во вторых скобках — значения для вставки. Здесь мы не указываем id — он будет вычисляться автоматически.
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO students (name, surname) VALUES ("Иван", "Иванов");')
#     cursor.execute('INSERT INTO students (name, surname) VALUES ("Петр", "Петров");')
#     cursor.execute('INSERT INTO students (name, surname) VALUES ("Анна", "Аннова");')
#     conn.commit()

"""
Сделаем запрос посложнее. Выберем студентов с id > 1 и получим только поля id и surname:
sqlite> SELECT id, surname FROM students WHERE id > 1;
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('SELECT id, surname FROM students WHERE id > 1;')
#     print(cursor.fetchall())

"""
Если мы хотим более сложное условие, можно использовать операторы AND или OR:
SELECT id, surname FROM students WHERE id > 1 AND surname like '%ова';
Так мы получим всех студентов с фамилией на -ова и id > 1.
Знак процента говорит о том, что перед окончанием «ова» есть какие-то символы.
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('SELECT id, surname FROM students WHERE id > 1 AND surname like "%ова";')
#     print(cursor.fetchall())

"""
Редактирование записей
Анна вышла замуж за Петра и решила взять его фамилию. Давайте поправим это с помощью оператора UPDATE:
sqlite> UPDATE students SET surname = 'Петрова' WHERE id = 3;
sqlite> SELECT * FROM students;
В WHERE мы указываем критерий, по которому должны изменить поля в SET. 
У Анны был id = 3, поэтому её легко по нему найти и изменить surname.
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('UPDATE students SET surname = "Петрова" WHERE id = 3;')
#     conn.commit()
#     cursor.execute('SELECT * FROM students;')
#     print(cursor.fetchall())

"""
Удаление записей
Иван Иванов был умным парнем, но долги есть долги. Ивана отчислили, поэтому удалим его из таблицы.
sqlite> DELETE FROM students WHERE id = 1;
sqlite> SELECT * FROM students;
"""
# with sqlite3.connect('database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('DELETE FROM students WHERE id = 1;')
#     conn.commit()
#     cursor.execute('SELECT * FROM students;')
#     print(cursor.fetchall())
