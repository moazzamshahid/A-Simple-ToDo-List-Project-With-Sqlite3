import sqlite3

class Database_Connection:
    def __init__(self,database) -> None:
        self.connection= None
        self.database=database
    
    def __enter__(self):
        self.connection=sqlite3.connect(self.database)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val,exc_tb):
        self.connection.commit()
        self.connection.close()
        
