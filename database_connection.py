import sqlite3

class DatabaseConnection:

    def __init__(self,host):
        self.coonnection = None
        self.host = host

    def __enter__(self):
        self.coonnection = sqlite3.connect(self.host)
        return self.coonnection

    def __exit__(self,exc_type,exc_val,exc_tab):
        self.coonnection.commit()
        self.coonnection.close()