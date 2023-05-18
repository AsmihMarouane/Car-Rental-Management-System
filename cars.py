from dataBaseLogin import *
import mysql.connector
class Car:
    def __init__(self, registration_number=None,brand=None, model=None, image=None, fuel_type=None, number_of_seats=None, transmission=None,
                 daily_rental_price=None, availability=None):
        if registration_number and brand and model and image and fuel_type and number_of_seats and transmission and daily_rental_price and availability:
            self.registration_number=registration_number
            self.brand = brand
            self.model = model
            self.image = image
            self.fuel_type = fuel_type
            self.number_of_seats = number_of_seats
            self.transmission = transmission
            self.daily_rental_price = daily_rental_price
            self.availability = availability
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
                        registration_number VARCHAR(255) ,
                        brand VARCHAR(255),
                        model VARCHAR(255),
                        image VARCHAR(255),
                        fuel_type VARCHAR(255),
                        number_of_seats INT,
                        transmission VARCHAR(255),
                        daily_rental_price DECIMAL(10, 2),
                        availability VARCHAR(255)
                        );
                    """)
            self.db.commit()

    def add_car(self):
        query = '''
            INSERT INTO cars (registration_number,brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (self.registration_number,self.brand, self.model, self.image, self.fuel_type, self.number_of_seats, self.transmission,
                    self.daily_rental_price, self.availability)
        self.db.execute(query, values)
        self.db.commit()

    def get_car_with_registration_number(self,car_id):
        query = '''
            SELECT * FROM cars WHERE registration_number = %s
        '''
        self.db.execute(query, (car_id,))
        result = self.db.cursor.fetchone()
        if result:
            return result
        else:
            return None

    def get_car(self,car_id):
        query = '''
            SELECT brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability
            FROM cars
            WHERE id = %s
        '''
        self.db.execute(query, (car_id,))
        result = self.db.cursor.fetchone()
        if result:
            return {
                "brand": result[0],
                "model": result[1],
                "image": result[2],
                "fuel_type": result[3],
                "number_of_seats": result[4],
                "transmission": result[5],
                "daily_rental_price": result[6],
                'availability': result[7]
            }
        else:
            return None

    def get_all_car(self):
        query = '''
            SELECT registration_number, brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability
            FROM cars
            
        '''
        self.db.execute(query)
        result = self.db.cursor.fetchall()
        return result


    def set_car(self, registration_number, brand, model, image, fuel_type,number_of_seats, transmission,daily_rental_price, availability):
        query = '''
            UPDATE cars
            SET brand = %s, model = %s, image = %s, fuel_type = %s, number_of_seats = %s, transmission = %s, daily_rental_price = %s, availability = %s
            WHERE registration_number = %s
        '''
        values = (brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability, registration_number)
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

    def add_car_to_database(self, registration_number, brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability):
        query = '''
            INSERT INTO cars (registration_number, brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        values = (registration_number, brand, model, image, fuel_type, number_of_seats, transmission, daily_rental_price, availability)
        self.db.execute(query, values)
        self.db.commit()

    def delete(self, car_id):
        query = "DELETE FROM cars WHERE registration_number = %s "
        values = (car_id,)
        self.db.execute(query, values)
        self.db.commit()
