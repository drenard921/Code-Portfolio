import sys
sys.path.append("../util/*")
sys.path.append("../db/*")
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql


# big question: Do we even need to write this data module

# Need to review how to write this method 
# basically double check your implementation
# what would an appointment class need to do other functions?
#  
class Appointment:
    def __init__(self, appointID, vaccine_name, time, caregiver, patient):
        self.appointID = appointID
        self.vaccine_name = vaccine_name
        self.time = time
        self.caregiver = caregiver
        self.patient = patient

    # get method for a specific Appointment
    def get(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor(as_dict=True)
        get_appointments = "SELECT * FROM Appointments WHERE AppointID = %s"
        try:
            cursor.execute(get_appointments, self.appointID)
            for row in cursor:
                self.vaccine_name = row['Vaccine_name']
                self.time = row['Time']
                self.caregiver = row['Caregiver']
                self.patient = row['Patient']
        except pymssql.Error:
            print("Error occurred when searching for appointments scheduled")
            cm.close_connection()
        cm.close_connection()
        return None

    def get_appointID(self):
        return self.appointID

    def get_vaccine_name(self):
        return self.vaccine_name

    def get_time(self):
        return self.time
    
    def get_caregiver(self):
        return self.caregiver

    def get_patient(self):
        return self.patient


    # saving to database
    # basically config how new values get entered into the db
    def save_to_db(self):
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()
        add_appointments = "INSERT INTO Appointments VALUES (%s, %s, %s, %s, %s);"
        try:
            cursor.execute(add_appointments, 
                           (self.appointID, 
                            self.vaccine_name, 
                            self.time, 
                            self.caregiver, 
                            self.patient))
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error as db_err:
            print("Error occurred when inserting Appointment")
            sqlrc = str(db_err.args[0])
            print("Exception code: " + str(sqlrc))
            cm.close_connection()
        cm.close_connection()

    def all_appointments():
        appointments = []
        cm = ConnectionManager()
        conn = cm.create_connection()
        select_doses = "SELECT * FROM Appointments;"
        try:
            cursor = conn.cursor(as_dict=True)
            cursor.execute(select_doses)
            for row in cursor:
                appointments.append(row)

        except pymssql.Error:
            print("Error occurred when checking Appointments")
            cm.close_connection()
        cm.close_connection() 
        return appointments
    
    # helper method to generate new Appointment IDs 
    def generate_appoint_id():
        cm = ConnectionManager()
        conn = cm.create_connection()
        select_current_id_count = "SELECT TOP (1) * FROM Appointments ORDER BY AppointID DESC;" 
        try:
            cursor = conn.cursor(as_dict=True)
            cursor.execute(select_current_id_count)
            for row in cursor:
                if row is None:
                    return 1
                else:
                    current_max = int(row['AppointID'])
                    new_max = current_max + 1
                    return new_max 
            return 1

        except pymssql.Error:
            print("Error occurred when generating a new appointID")
            cm.close_connection()
        cm.close_connection()


    def delete_appointment(appoint_id):
        # maybe add checks here
        cm = ConnectionManager()
        conn = cm.create_connection()
        cursor = conn.cursor()
        delete_appointment = "DELETE FROM Appointments WHERE AppointID = %s;"
        try:
            cursor.execute(delete_appointment, appoint_id)
            # you must call commit() to persist your data if you don't set autocommit to True
            conn.commit()
        except pymssql.Error:
            print("Error occurred removing Caregiver availability")
            cm.close_connection()
        cm.close_connection()   
