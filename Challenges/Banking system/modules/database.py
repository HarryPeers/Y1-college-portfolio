import sqlite3 

class database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.check_table()

    def create_table(self):
        cursor = self.cursor
        cursor.execute("CREATE TABLE accounts ( pin TEXT, balance BIGINT);")
        self.connection.commit()

        print("created table")

    def check_table(self, create:bool=True):
        cursor = self.cursor
        cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchone()

        if tables is None or "accounts" not in tables and create:
            self.create_table()

        return tables is None or "accounts" in tables
            

        
    @property
    def cursor(self):
        return self.connection.cursor()