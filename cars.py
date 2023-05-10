from dataBaseLogin import *
import mysql.connector
class Car:
    def __init__(self, marque=None, modele=None, image=None, type_de_carburant=None, nombre_de_places=None, transmission=None, prix_location_par_jour=None, disponibilite=None):
        if marque and modele and image and type_de_carburant and nombre_de_places and transmission and prix_location_par_jour and disponibilite :
            self.marque = marque
            self.modele = modele
            self.image = image
            self.type_de_carburant = type_de_carburant
            self.nombre_de_places = nombre_de_places
            self.transmission = transmission
            self.prix_location_par_jour = prix_location_par_jour
            self.disponibilite = disponibilite
        else:
            self.db = Database()

    def create_table(self):
        self.db.execute("SHOW TABLES LIKE 'cars '")
        result = self.db.cursor.fetchone()
        if result:
            return
        else:
            self.db.execute("""
                        CREATE TABLE cars (
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            marque VARCHAR(255),
                            modele VARCHAR(255),
                            image VARCHAR(255),
                            type_de_carburant VARCHAR(255),
                            nombre_de_places INT,
                            transmission VARCHAR(255),
                            prix_location_par_jour DECIMAL(10, 2),
                            disponibilite VARCHAR(255)
                        )
                    """)
            self.db.commit()

    def add_car(self):
        query = '''
            INSERT INTO cars (marque, modele, image, type_de_carburant, nombre_de_places, transmission, prix_location_par_jour, disponibilite)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (self.marque, self.modele, self.image, self.type_de_carburant, self.nombre_de_places, self.transmission,
                    self.prix_location_par_jour, self.disponibilite)
        self.db.execute(query, values)
        self.db.commit()

    def get_car(self,car_id):
        query = '''
            SELECT marque, modele, image, type_de_carburant, nombre_de_places, transmission, prix_location_par_jour, disponibilite
            FROM cars
            WHERE id = %s
        '''
        self.db.execute(query, (car_id,))
        result = self.db.cursor.fetchone()
        if result:
            return {
                "marque": result[0],
                "modele": result[1],
                "image": result[2],
                "type_de_carburant": result[3],
                "nombre_de_places": result[4],
                "transmission": result[5],
                "prix_location_par_jour": result[6],
                'disponibilite': result[7]
            }
        else:
            return None

    def set_car(self, car_id):
        query = '''
            UPDATE cars
            SET marque = %s, modele = %s, image = %s, type_de_carburant = %s, nombre_de_places = %s, transmission = %s, prix_location_par_jour = %s, disponibilite = %s
            WHERE id = %s
        '''
        values = (
        self.marque, self.modele, self.image, self.type_de_carburant, self.nombre_de_places, self.transmission,
        self.prix_location_par_jour, self.disponibilite, car_id)
        self.db.execute(query, values)
        self.db.commit()

    def get_number_of_cars(self):
        query = '''
            SELECT COUNT(*) FROM cars
        '''
        self.db.execute(query)
        result = self.db.cursor.fetchone()
        if result:
            return result[0]  # add the index to retrieve the count of the cars
        else:
            return 0  # return 0 if there is no result