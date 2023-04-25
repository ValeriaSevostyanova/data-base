import sqlite3  # специальная библиотека для создания базы данных и работы с ней
class Data_base:  # класс для БД

    def __init__(self) -> None:  # созаем подключение
        self.sqlite_connection = sqlite3.connect('sqlite_python_dima.db')  # либо создаем саму базу данных
        # либо подключаемся к ней , благодаря connect
        self.cursor = self.sqlite_connection.cursor()
        print('Соединение установлено...\nOpen')

    def test_connect(self):  # проверяем подклчюение
        sqlite_select_query = "select sqlite_version();"  # создается запрос на версию БД
        self.cursor.execute(sqlite_select_query)  # добаляем запрос БД
        record = self.cursor.fetchall()  # получаем все то что вернет в ответ БД
        print("Версия базы данных SQLite: ", record)  # выводим ответ БД

    def create_table(self):  # создает таблицу
        sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL);'''
        self.cursor.execute(sqlite_create_table_query)
        print("Таблица SQLite создана")

    def insert_value(self):  # добавление данных
        sqlite_insert_query = """INSERT INTO sqlitedb_developers
                          (id, name)  VALUES  (1, 'Dima')"""
        self.cursor.execute(sqlite_insert_query)
        print('Добавили значение в таблицу')

    def select_from(self):  # получение данных
        test_list = list(self.cursor.execute(
            """select * from sqlitedb_developers """))  # получение данных из таблицы, блягодаря запросу# отправляем запрос
        print('Запрос на получение данных отпрвлен...')
        print(test_list)

    def __del__(self):  # закрывает соединение
        self.sqlite_connection.commit()
        self.cursor.close()
        print('Соединение закрыто...\nClose')


table_test = Data_base()
table_test.test_connect()
table_test.create_table()
table_test.insert_value()
table_test.select_from()