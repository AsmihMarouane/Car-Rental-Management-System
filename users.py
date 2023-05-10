from dataBaseLogin import Database
import mysql.connector
import hashlib
class User:
    def __init__(self, username=None, password=None, nom=None, prenom=None, telephone=None, email=None,user_type=None):
        if username and password and nom and prenom and telephone and email:
            self.id = None # Auto-incremented by the database
            self.username = username
            self.password = password
            self.nom = nom
            self.prenom = prenom
            self.telephone = telephone
            self.email = email
            self.user_type=user_type
        else:
            self.db = Database()
    def create_table(self):
        self.db.execute("SHOW TABLES LIKE 'users'")
        result = self.db.cursor.fetchone()
        if result:
            return
        else:
            self.db.execute("""
                        CREATE TABLE users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(255) NOT NULL UNIQUE,
                            password VARCHAR(255) NOT NULL,
                            nom VARCHAR(255) NOT NULL,
                            prenom VARCHAR(255) NOT NULL,
                            telephone VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL,
                            user_type ENUM('user', 'admin') DEFAULT 'user'
                        )
                    """)
            self.db.commit()
    def add_user(self, username, password, email):
        # add new user with default user_type as "user"
        sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        val = (username, hashed_password, email)
        self.db.execute(sql, val)
        self.db.commit()
    def verify_login(self, username, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (username, hashed_password)
        self.db.execute(sql, val)
        result = self.db.cursor.fetchone()
        if result:
            return True
        else:
            return False
    def login_exist(self, username):
        sql = "SELECT * FROM users WHERE username = %s"
        self.db.execute(sql, (username,))
        result = self.db.cursor.fetchone()
        if result:
            return False
        else:
            return True
    def get_user(self, username):
        sql = "SELECT * FROM users WHERE username = %s"
        val = (username,)
        self.db.execute(sql, val)
        result = self.db.cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "password": result[2],
                "nom": result[3],
                "prenom": result[4],
                "telephone": result[5],
                "email": result[6],
                'user_type': result[7]
            }
        else:
            return None

    def set_user(self, username, nom=None, prenom=None, numero_telephone=None, email=None, user_type=None):
        sql = "UPDATE users SET nom = %s, prenom = %s, numero_telephone = %s, email = %s, user_type = %s WHERE username = %s"
        val = (nom, prenom, numero_telephone, email, user_type, username)
        self.db.execute(sql, val)
        self.db.commit()
    def change_password_without_hashing(self, username, password):
        sql = "UPDATE users SET password = %s WHERE username = %s"
        val = (password, username)
        self.db.execute(sql, val)
        self.db.commit()
    def change_nom_prenom(self, username, nom, prenom):
        sql = "UPDATE users SET nom = %s, prenom = %s WHERE username = %s"
        val = (nom, prenom, username)
        self.db.execute(sql, val)
        self.db.commit()
    def change_numero_telephone(self, username, numero_telephone):
        sql = "UPDATE users SET telephone = %s WHERE username = %s"
        val = (numero_telephone, username)
        self.db.execute(sql, val)
        self.db.commit()
    def change_email(self, username, email):
        sql = "UPDATE users SET email = %s WHERE username = %s"
        val = (email, username)
        self.db.execute(sql, val)
        self.db.commit()
    def change_user_type(self, username, user_type):
        sql = "UPDATE users SET user_type = %s WHERE username = %s"
        val = (user_type, username)
        self.db.execute(sql, val)
        self.db.commit()