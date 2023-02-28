import sys
sys.path.append("../db/*")
from db.ConnectionManager import ConnectionManager
import pymssql


class Vaccine:
    def __init__(self, vaccine_name, available_doses):
        self.vaccine_name = vaccine_name
        self.available_doses = available_doses

    # getters
    def get(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        get_vaccine = "SELECT Name, Doses FROM Vaccines WHERE Name = %s"
        try:
            cursor.execute(get_vaccine, self.vaccine_name)
            for row in cursor:
                self.available_doses = row['Doses']
                return self
        except pymssql.Error:
            print("Error occurred when getting Vaccine")
            cm.close_connection()
        cm.close_connection()
        return None

    def get_vaccine_name(self):
        return self.vaccine_name

    def get_available_doses(self):
        return self.available_doses

    # uploading to database
    def save_to_db(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        add_doses = "INSERT INTO VACCINES VALUES (%s, %d)"
        try:
            cursor.execute(add_doses, (self.vaccine_name, self.available_doses))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            print("Error occurred when insert Vaccines")
            cm.close_connection()
        cm.close_connection()

    # Increment the available doses
    def increase_available_doses(self, num):
        if num <= 0:
            ValueError("Argument cannot be negative!")
        self.available_doses += num

        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        update_vaccine_availability = "UPDATE vaccines SET Doses = %d WHERE name = %s"
        try:
            cursor.execute(update_vaccine_availability, (self.available_doses, self.vaccine_name))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            print("Error occurred when updating vaccine availability")
            cm.close_connection()
        cm.close_connection()

    # Decrement the available doses
    def decrease_available_doses(self, num):
        if self.available_doses - num < 0:
            ValueError("Not enough available doses!")
        self.available_doses -= num

        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()

        update_vaccine_availability = "UPDATE vaccines SET Doses = %d WHERE name = %s"
        try:
            cursor.execute(update_vaccine_availability, (self.available_doses, self.vaccine_name))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            print("Error occurred when updating vaccine availability")
            cm.close_connection()
        cm.close_connection()

    # helper method to find all vaccines currently in inventory
    # returns a dictionary of all available vaccines
    def vaccine_inventory():
        doses = {}
        cm = ConnectionManager()
        conn = cm.create_connection()
        select_doses = "SELECT * FROM Vaccines;"
        try:
            cursor = conn.cursor(as_dict=True)
            cursor.execute(select_doses)
            #  returns false if the cursor is not before the first record or if there are no rows in the ResultSet.
            for row in cursor:
                if row['Doses'] > 1:
                    doses[row['Name']] = row['Doses']

        except pymssql.Error:
            print("Error occurred when checking Vaccine Availibility")
            cm.close_connection()
        cm.close_connection()
        return doses         

    def __str__(self):
        return f"(Vaccine Name: {self.vaccine_name}, Available Doses: {self.available_doses})"
