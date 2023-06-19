'''
ЗДЕСЬ СОЗДАЕМ БД, В НЕЙ ТАБЛИЦУ, В НЕЙ ИНФОРМАЦИЮ
'''
# база данных
import sqlite3  # специальная библиотека для создания базы данных и работы с ней

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')  # либо создаем саму базу данных
    # либо подключаемся к ней , благодаря connect
    sqlite_insert_query = """INSERT INTO sqlitedb_developers 
                          (id, name)  VALUES  (2, 'Dima')"""
    # составляем запрос в базу данных в указзанную таблицу
    # запрос сторится блягодаря языку SQL
    #  существуют различные базы данных , например MySQL, PostgreSQL, SQLite, mongoDB,ORACLE
    # в целом запросы везде одинаковые но есть все равно различия
    # create table - создание таблицы
    # insert into - запись данных в таблицу
    # select * from - получение данных из таблицы

    cursor = sqlite_connection.cursor()  # создание курсора для отправки запросов в БД
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_insert_query)  # отправляем запрос
    # execute - отправляет и получает данные из БД
    test_list = list(
        cursor.execute("""select * from sqlitedb_developers """))  # получение данных из таблицы, блягодаря запросу
    sqlite_connection.commit()  # сохранение БД
    print("Таблица SQLite добавила данные")
    print(test_list)
    cursor.close()  # закрытие соединения

except sqlite3.Error as error:  # обработка ошибок в случае если не подключилист к БД
    print("Ошибка при подключении к sqlite", error)  # error ошибка
finally:  # отработает в любом случае не важно что сработало try или except
    if (sqlite_connection):  # закрытие соединения в любом случае
        sqlite_connection.close()  # закрытие соединения
        print("Соединение с SQLite закрыто")

# sqlitedb_developers -название таблицы
### Создание таблица
'''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL);'''
### для заполнения данными
'''INSERT INTO sqlitedb_developers
                         (id, name)  VALUES  (1, 'Демо ИМЯ')'''

### для получения данных
'''select * from sqlitedb_developers '''