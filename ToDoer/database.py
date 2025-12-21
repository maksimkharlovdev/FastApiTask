import os
import sqlite3
from sqlite3 import Connection, IntegrityError


class Database():
    path: str
    connection: Connection
    def __init__(self):
        self.path = os.getenv("TODOER_DB_PATH")
        print(self.path)
        self.connection = sqlite3.connect(self.path)
        self.connection.execute('''CREATE TABLE IF NOT EXISTS Tasks (
        title TEXT NOT NULL PRIMARY KEY, 
        description TEXT, 
        completed BOOLEAN);
        ''')
        self.connection.commit()
        self.connection.close()


    def add(self, title, description='без описания'):
        self.connection = sqlite3.connect(self.path)
        try:
            self.connection.execute(f"INSERT INTO Tasks (title, description, completed) VALUES ("
                                f"'{title}', '{description}', '{False}' );")
        except IntegrityError:
            self.connection.commit()
            self.connection.close()
            return self.update(title,description)
        self.connection.commit()
        self.connection.close()



    def get(self, title = None):
        self.connection = sqlite3.connect(self.path)
        if title:
            result = self.connection.execute(f"SELECT * FROM Tasks WHERE title='{title}';").fetchall()[0]
        else:
            result = self.connection.execute(f"SELECT * FROM Tasks;").fetchall()
        self.connection.close()
        return result


    def delete(self, title):
        self.connection = sqlite3.connect(self.path)
        self.connection.execute(f"DELETE FROM Tasks WHERE title='{title}';")
        self.connection.commit()
        self.connection.close()


    def update(self, title, description, completed = False):
        self.connection = sqlite3.connect(self.path)
        self.connection.execute(f"UPDATE Tasks SET description='{description}', completed='{completed}' WHERE title = '{title}';")
        self.connection.commit()
        self.connection.close()

