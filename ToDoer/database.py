import os
import sqlite3

class Database():
    path = os.getenv("TODOER_DB_PATH")

    def __init__(self):
        pass