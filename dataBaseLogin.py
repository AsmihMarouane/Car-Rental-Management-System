import mysql.connector
import hashlib
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="carlux"
        )
        self.cursor = self.connection.cursor()
    def execute(self, query, params=None):
        self.cursor.execute(query, params)

    def commit(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()