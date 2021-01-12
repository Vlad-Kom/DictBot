import sqlite3

from data import database_name


class Database:
    def __init__(self, path_to_db=database_name):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        print(self.path_to_db)
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def add_user(self, id: int, name: str):
        sql = "INSERT INTO user(id_user, name) VALUES(?, ?)"
        parametres = (id, name)
        self.execute(sql, parameters=parametres, commit=True)


    def add_word(self, id: int, word: str, lang: str):
        sql = "INSERT INTO word(id_user, word, lang, value) VALUES(?, ?, ?, 0)"
        parametres = (id, word, lang)
        return self.execute(sql, parameters=parametres, commit=True)

    def check_user(self, id: int):
        sql = "SELECT * FROM user WHERE id_user = ?"
        parametres = (id,)
        return self.execute(sql, parameters=parametres, fetchone=True)

    def check_word(self, id: int, word: str):
        sql = "SELECT * FROM word WHERE id_user = ? AND word = ?"
        parametres = (id, word,)
        return self.execute(sql, parameters=parametres, fetchone=True)

    def zero_value_word(self, id: int, word: str):
        sql = "UPDATE word SET value = 0 WHERE id_user = ? AND word = ?"
        parametres = (id, word,)
        return self.execute(sql, parameters=parametres, commit=True)
    def increase_value_word(self, id: int, word: str):
        sql = "UPDATE word SET value = value + 1 WHERE id_user = ? AND word = ?"
        parametres = (id, word,)
        return self.execute(sql, parameters=parametres, commit=True)

    def delete_word(self, id: int, word: str):
        sql = "DELETE FROM word WHERE id_user = ? AND word = ?"
        parametres = (id, word,)
        return self.execute(sql, parameters=parametres, commit=True)

    def delete_all_words(self, id: int, lang: str):
        sql = "DELETE FROM word WHERE id_user = ? AND lang = ?"
        parametres = (id, lang,)
        return self.execute(sql, parameters=parametres, commit=True)

    def set_words(self, id: int, lang: str):
        sql = "SELECT DISTINCT word FROM word WHERE id_user = ? AND lang = ? ORDER BY random() LIMIT 4"
        parametres = (id, lang)
        return self.execute(sql, parameters=parametres, fetchall=True)

def logger(statement):
    print(f"""
________________________________________________________________________________
Executing:
{statement}
________________________________________________________________________________
""")
