from .database import database

class account:
    def __init__(self, db:database, pin:int, create_missing:bool=False):
        self.database = db
        self.pin = pin
        self._record = None
        self._balance = 0

        if not self.exists:
            self.create()

    @property
    def record(self) -> tuple:
        if self._record is None:
            cursor = self.database.cursor
            cursor.execute(f"SELECT * FROM accounts WHERE pin={self.pin}")
            self._record = cursor.fetchone()
            self.balance = self._record[1]
        return self._record

    @property
    def exists(self) -> bool:
        return self.record is not None
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value:int):
        self._balance += value
        cursor = self.database.cursor
        cursor.execute(f"UPDATE accounts SET balance={self.balance} WHERE pin={self.pin} ")
        self.database.connection.commit()

    def withdraw(self, amount:int):
        self._balance -= amount
        cursor = self.database.cursor
        cursor.execute(f"UPDATE accounts SET balance={self.balance} WHERE pin={self.pin} ")
        self.database.connection.commit()

    def create(self):
        print("creating")

        cursor = self.database.cursor
        cursor.execute(f"INSERT INTO accounts VALUES ({self.pin}, 0)")
        self.database.connection.commit()
        
        self._record = None
