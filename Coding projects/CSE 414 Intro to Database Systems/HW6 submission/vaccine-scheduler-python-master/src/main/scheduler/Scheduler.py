import sys
from model.Vaccine import Vaccine
from model.Caregiver import Caregiver
from model.Patient import Patient
from model.Appointment import Appointment
from util.Util import Util
from db.ConnectionManager import ConnectionManager
import pymssql
import datetime
import random


'''
objects to keep track of the currently logged-in user
Note: it is always true that at most one of currentCaregiver and currentPatient is not null
        since only one user can be logged-in at a time
'''
current_patient = None

current_caregiver = None


def create_patient(tokens):
    # check 1: the length for tokens need to be exactly 3 to 
    # include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return

    username = tokens[1]
    password = tokens[2]
    # check 2: check if the username has been taken already
    if username_exists(username, "Patients"):
        print("Username taken, try again!")
        return

    salt = Util.generate_salt()
    hash = Util.generate_hash(password, salt)

    # create the patient
    try:
        patient = Patient(username, salt=salt, hash=hash)
        # save to patient information to our database
        patient.save_to_db()
        print(" *** Account created successfully *** ")
    except pymssql.Error:
        print("Create failed")
        return


def create_caregiver(tokens):
    # create_caregiver <username> <password>
    # check 1: the length for tokens need to be exactly 3 
    # to include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return
    username = tokens[1]
    password = tokens[2]
    # check 2: check if the username has been taken already
    if username_exists(username, "Caregivers"):
        print("Username taken, try again!")
        return
    salt = Util.generate_salt()
    hash = Util.generate_hash(password, salt)
    # create the caregiver
    try:
        caregiver = Caregiver(username, salt=salt, hash=hash)
        # save to caregiver information to our database
        caregiver.save_to_db()
        print(" *** Account created successfully *** ")
    except pymssql.Error:
        print("Create failed")
        return


def username_exists(username, db_name):
    cm = ConnectionManager()
    conn = cm.create_connection()
    select_username = "SELECT * FROM " + db_name + " WHERE Username = %s"
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select_username, username)
        for row in cursor:
            return row['Username'] is None
    except pymssql.Error:
        print("Error occurred when checking username")
        cm.close_connection()
    cm.close_connection()
    return False


def login_patient(tokens):
    # check 1: if someone's already logged-in, they need to log out first
    global current_patient
    if current_patient is not None or current_caregiver is not None:
        print("Already logged-in!")
        return
    # check 2: the length for tokens need to be exactly 3 
    # to include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return
    username = tokens[1]
    password = tokens[2]
    patient = None
    try:
        patient = Patient(username, password=password).get()
    except pymssql.Error:
        print("Error occurred when logging in")

    # check if the login was successful
    if patient is None:
        print("Please try again!")
    else:
        print("Patient logged in as: " + username)
        current_patient = patient


def login_caregiver(tokens):
    # check 1: if someone's already logged-in, they need to log out first
    global current_caregiver
    if current_caregiver is not None or current_patient is not None:
        print("Already logged-in!")
        return
    # check 2: the length for tokens need to be exactly 3 to include 
    # all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return
    username = tokens[1]
    password = tokens[2]
    caregiver = None
    try:
        caregiver = Caregiver(username, password=password).get()
    except pymssql.Error:
        print("Error occurred when logging in")
    if caregiver is None:
        print("Please try again!")
    else:
        print("Caregiver logged in as: " + username)
        current_caregiver = caregiver


def search_caregiver_schedule(tokens):
    global current_patient
    global current_caregiver
    # check 1: make sure we are logged in
    if current_caregiver is None and current_patient is None:
        print("Must login to search caregiver schedule")
        print("please try logging in or creating an account to see vaccine schedule")
        return
    # check 2: the length for tokens need to be exactly 2 to include all information (with the operation name)
    if len(tokens) != 2:
        print("Please try again!")
        return
    input_date = tokens[1]

    # checking input date
    if input_date is "" or None:
        print("no date entry detected")
        print("Please try again!")
        print("Desired date format is MM-DD-YYYY")
        return
    if type(input_date) != str:
        print("Please try again!")
        print("Desired date format is MM-DD-YYYY")
        return
    if len(input_date) != 10:
        print("Incorrect date entry detected")
        print("Desired date format is MM-DD-YYYY")
        print("Please try again!")
        return
             

    # assume input is hyphenated in the format mm-dd-yyyy
    date_tokens = input_date.split("-")
    month = int(date_tokens[0])
    day = int(date_tokens[1])
    year = int(date_tokens[2])
    date = str(datetime.datetime(year, month, day))

    # making lists for printing:
    caregivers = []
    doses = {}
    # query call for this method
    cm = ConnectionManager()
    conn = cm.create_connection()
    select_caregivers = "SELECT Caregiver FROM Availabilities WHERE Time = %s" 
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select_caregivers, date)
        #  returns false if the cursor is not before the first record or if there are no rows in the ResultSet.
        for row in cursor:
            if (row['Caregiver'] is not None):
                caregivers.append(row['Caregiver'])
    except pymssql.Error:
        print("Error occurred when checking Caregiver Availibility")
        cm.close_connection()
    cm.close_connection()

    # trying to find the vaccine doses
    doses = Vaccine.vaccine_inventory()

    # we want the Caregivers availible
    if (caregivers is None):
        print("No caregivers availibile on this date")
        print("please try another date")
        return
    if (doses is None):
        print("Currently no doses availible for appointments")
        print("please check back later for availibility on another date")
    
    print("Caregivers avalible on this date:")
    for name in caregivers:
        print(name + " is availible on " + date)

    print("Available Doses:")
    print(Vaccine.vaccine_inventory())
    

def reserve(tokens):
    # Patients perform this operation to reserve an appointment
    # You will be randomly assigned a caregiver for the reservation on that date.
    # Output the assigned caregiver and the appointment ID for the reservation

    # Check that a user is logged in
        # simple log-in check
    global current_patient
    # check 1: make sure we are logged in
    if current_patient is None:
        print("Must login as a patient to reserve an appointment")
        print("please try logging in or creating an account to schedule an appointment")
        return
        
    # check 2: the length for tokens need to be exactly 3
    #  to include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return

    # check that the date entry makes sense
        # several if statements
    input_date = tokens[1]

    if type(input_date) != str:
        print("Please try again!")
        print("Desired date format is MM-DD-YYYY")
        return

    if input_date is " " or "":
        print("Empty date entry detected")
        print("Please try again!")
        print("Desired date format is MM-DD-YYYY")
        return

    if len(input_date) != 10:
        print("Incorrect date entry detected")
        print("Desired date format is MM-DD-YYYY")
        print("Please try again!")
        return

    
    # assume input is hyphenated in the format mm-dd-yyyy
    date_tokens = input_date.split("-")
    month = int(date_tokens[0])
    day = int(date_tokens[1])
    year = int(date_tokens[2])
    date = str(datetime.datetime(year, month, day))

    # check that their vaccine entry makes sense
        # several if statements
    input_vaccine = tokens[2]
    
    if Caregiver.is_available_times(date) == False:
        print("There was no availability found on: " + str(date))
        print("Please try again picking a different date")
        return

    doses = Vaccine.vaccine_inventory()
    if input_vaccine not in doses:
        print("no vaccines were found with the name: " + input_vaccine)
        print("Please try again!")
        return

    if  doses[input_vaccine] <= 0:
        print("We are currently experiencing shortages of the " + input_vaccine + " vaccine")
        print("Please try again")
        print("Here are vaccines that are currently available:")
        for vax in doses:
            if doses[vax] > 0:
                print(vax)
        return 
    our_vax = Vaccine(input_vaccine, doses[input_vaccine])
    
    # Check that appointments are indeed available on this date
    caregivers = []
    cm = ConnectionManager()
    conn = cm.create_connection()
    select_caregivers = "SELECT Caregiver FROM Availabilities WHERE Time = %s" 
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select_caregivers, date)
        #  returns false if the cursor is not before the first record or if there are no rows in the ResultSet.
        for row in cursor:
            caregivers.append(row['Caregiver'])
    except pymssql.Error:
        print("Error occurred when checking Caregiver Availibility")
        cm.close_connection()
    cm.close_connection()

    if caregivers is None:
        print("No available appointments on this day")
        print("Please try another date!")
        return
    
    # randomly picking a caregiver from caregivers available
    our_caregiver = caregivers[random.randint(0, len(caregivers) -1)]

    # Add their appointment to the appointment table
    our_patient = current_patient.get_username()
    apt_id = Appointment.generate_appoint_id()
    apt = Appointment(apt_id, input_vaccine, date, our_caregiver, our_patient)
    apt.save_to_db()

    # update associated tables
    Caregiver.delete_availability(our_caregiver, date)
    our_vax.decrease_available_doses(1)

    # print result
    print("**** Appoinment on " + str(date)[0:11] + "reserved ****")
    print("Appointment with caregiver: " + str(our_caregiver))
    print("AppointID is: " + str(apt_id))
    

def upload_availability(tokens):
    #  upload_availability <date>
    #  check 1: check if the current logged-in user is a caregiver
    global current_caregiver
    if current_caregiver is None:
        print("Please login as a caregiver first!")
        return
    # check 2: the length for tokens need to be exactly 2 
    # to include all information (with the operation name)
    if len(tokens) != 2:
        print("Please try again!")
        return
    date = tokens[1]
    # assume input is hyphenated in the format mm-dd-yyyy
    date_tokens = date.split("-")
    month = int(date_tokens[0])
    day = int(date_tokens[1])
    year = int(date_tokens[2])
    try:
        d = datetime.datetime(year, month, day)
        try:
            current_caregiver.upload_availability(d)
        except:
            print("Upload Availability Failed")
        print("Availability uploaded!")
    except ValueError:
        print("Please enter a valid date!")
    except pymssql.Error as db_err:
        print("Error occurred when uploading availability")


def cancel(tokens):
    # take in appropriate id number
    if current_patient is None and current_caregiver is not None:
        print("must be logged in to cancel appointments")
        print("Please try again!")
        return
    # check 2: the length for tokens need to be exactly 3 
    # to include all information (with the operation name)
    if len(tokens) != 2:
        print("Please try again!")
        return
    apt_id = tokens[1]
    # grabbing appointment info to then be added back to availabilities
    apt = {}
    cm = ConnectionManager()
    conn = cm.create_connection()
    select__cancel_appointment_ = "SELECT * FROM Appointments WHERE appointID = %s;"
    try:
        cursor = conn.cursor(as_dict=True)
        cursor.execute(select__cancel_appointment_, apt_id)
        for row in cursor:
            apt['Time'] = row['Time']
            apt['Caregiver'] = row['Caregiver']
            apt['Vaccine_name'] = row['Vaccine_name']
    except pymssql.Error:
        print("Error occurred when searching for appointment with id " 
              + apt_id)
        print("Appointment numbers must be intergers")
        print("please try again with valid appointment id number")
        cm.close_connection()
    cm.close_connection()

    if(not apt):
        print("Error occurred when searching for appointment with id " 
              + apt_id)
        print("No appointments with that ID found")
        print("please try again with valid appointment id number")
        return

    # adding availability back to table
    Caregiver.upload_availability_with_name(apt['Caregiver'], apt['Time'])
    # adding dose back to table
    doses = Vaccine.vaccine_inventory()
    our_vax = Vaccine(apt['Vaccine_name'], doses[apt['Vaccine_name']])
    our_vax.increase_available_doses(1) 

    # deleting appointment
    Appointment.delete_appointment(apt_id)
    print("Appointment on " + str(apt['Time']) + 
          " || with AppointID: " + str(apt_id) + " cancelled")


def add_doses(tokens):
    #  add_doses <vaccine> <number>
    #  check 1: check if the current logged-in user is a caregiver
    global current_caregiver
    if current_caregiver is None:
        print("Please login as a caregiver first!")
        return

    #  check 2: the length for tokens need to be exactly 3 to include all information (with the operation name)
    if len(tokens) != 3:
        print("Please try again!")
        return

    vaccine_name = tokens[1]
    doses = int(tokens[2])
    vaccine = None
    try:
        try:
            vaccine = Vaccine(vaccine_name, doses).get()
        except:
            print("Failed to get Vaccine!")
            return
    except pymssql.Error:
        print("Error occurred when adding doses")

    # check 3: if getter returns null, it means that we need to create the vaccine and insert it into the Vaccines
    #          table

    if vaccine is None:
        try:
            vaccine = Vaccine(vaccine_name, doses)
            try:
                vaccine.save_to_db()
            except:
                print("Failed To Save")
                return
        except pymssql.Error:
            print("Error occurred when adding doses")
    else:
        # if the vaccine is not null, meaning that the vaccine already exists in our table
        try:
            try:
                vaccine.increase_available_doses(doses)
            except:
                print("Failed to increase available doses!")
                return
        except pymssql.Error:
            print("Error occurred when adding doses")

    print("Doses updated!")


def show_appointments(tokens):
    # check to make sure someone is logged in
    if current_caregiver is None and current_patient is None:
        print("Must login to show current appointments!")
        print("Please try again!")
        return
    
    # check to make sure just one token
    if len(tokens) != 1:
        print("Please try again!")
        return
    
    # set working user type
    # collect username
    if current_caregiver is not None:
        user_type = "Caregiver"
        alt_type = "Patient"
        username = current_caregiver.get_username()
        get_appointments = "SELECT * FROM Appointments WHERE Caregiver = %s;"

    if current_patient is not None:
        user_type = "Patient"
        alt_type = "Caregiver"
        username = current_patient.get_username()
        get_appointments = "SELECT * FROM Appointments WHERE Patient = %s;"


    # initialize result
    result = []
    cm = ConnectionManager()
    conn = cm.create_connection()
    cursor = conn.cursor(as_dict=True)
    try:
        cursor.execute(get_appointments, username)
        for row in cursor:
            result.append(row)
    except pymssql.Error:
        print("Error occurred when getting appointments")
        cm.close_connection()
    cm.close_connection()
    
    # pritn results
    print("*** Scheduled appointments for " + 
          user_type + ": " + username + " ***")
    if(not result):
        print("No current appointments found")
    else: 
        for row in result:
            a = str(row['AppointID'])
            v = row['Vaccine_name']
            d = str(row['Time'])
            pc = row[alt_type]
            print("Appointment ID: " + a + 
                  " || Vaccine: " + v + 
                  " || Date: " + d + " || " + 
                  alt_type + " : " + pc)


def logout(tokens):
    global current_patient
    global current_caregiver 
    curr_user = ""
    if current_patient is not None:
        curr_user = str(current_patient.get_username())
    
    if current_caregiver is not None:
        curr_user = str(current_caregiver.get_username())

    current_patient = None
    current_caregiver = None
    
    print("*** Account logout successful ***") 
    print("See you later " + curr_user + "!")


def start():
    stop = False
    while not stop:
        print()
        print(" *** Please enter one of the following commands *** ")
        print("> create_patient <username> <password>")  # //TODO: implement create_patient (Part 1)
        print("> create_caregiver <username> <password>")
        print("> login_patient <username> <password>")  #// TODO: implement login_patient (Part 1)
        print("> login_caregiver <username> <password>")
        print("> search_caregiver_schedule <date>")  #// TODO: implement search_caregiver_schedule (Part 2)
        print("> reserve <date> <vaccine>") #// TODO: implement reserve (Part 2)
        print("> upload_availability <date>")
        print("> cancel <appointment_id>") #// TODO: implement cancel (extra credit)
        print("> add_doses <vaccine> <number>")
        print("> show_appointments")  #// TODO: implement show_appointments (Part 2)
        print("> logout") #// TODO: implement logout (Part 2)
        print("> Quit")
        print()
        response = ""
        print("> Enter: ", end='')

        try:
            response = str(input())
        except ValueError:
            print("Type in a valid argument")
            break

        response = response.lower()
        tokens = response.split(" ")
        if len(tokens) == 0:
            ValueError("Try Again")
            continue
        operation = tokens[0]
        if operation == "create_patient":
            create_patient(tokens)
        elif operation == "create_caregiver":
            create_caregiver(tokens)
        elif operation == "login_patient":
            login_patient(tokens)
        elif operation == "login_caregiver":
            login_caregiver(tokens)
        elif operation == "search_caregiver_schedule":
            search_caregiver_schedule(tokens)
        elif operation == "reserve":
            reserve(tokens)
        elif operation == "upload_availability":
            upload_availability(tokens)
        elif operation == "cancel":
            cancel(tokens)
        elif operation == "add_doses":
            add_doses(tokens)
        elif operation == "show_appointments":
            show_appointments(tokens)
        elif operation == "logout":
            logout(tokens)
        elif operation == "quit":
            print("Thank you for using the scheduler, Goodbye!")
            stop = True
        else:
            print("Invalid Argument")


if __name__ == "__main__":
    '''
    // pre-define the three types of authorized vaccines
    // note: it's a poor practice to hard-code these values, but we will do this ]
    // for the simplicity of this assignment
    // and then construct a map of vaccineName -> vaccineObject
    '''

    # start command line
    print()
    print("Welcome to the COVID-19 Vaccine Reservation Scheduling Application!")

    start()
