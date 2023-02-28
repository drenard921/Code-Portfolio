CREATE TABLE Caregivers (
    Username varchar(255),
    Salt BINARY(16),
    Hash BINARY(16),
    PRIMARY KEY (Username)
);

CREATE TABLE Availabilities (
    Time date,
    Caregiver varchar(255) REFERENCES Caregivers(Username),
    PRIMARY KEY (Time, Caregiver)
);

CREATE TABLE Vaccines (
    Name varchar(255),
    Doses int,
    PRIMARY KEY (Name)
);

CREATE TABLE Patients (
    Username varchar(255),
    Salt BINARY(16),
    Hash BINARY(16),
    PRIMARY KEY (Username)
);

CREATE TABLE Appointments (
    AppointID INT,
    Vaccine_name varchar(255) REFERENCES Vaccines(Name),
    Time date,
    Caregiver varchar(255),
    Patient varchar(255) REFERENCES Patients(Username),
    PRIMARY KEY (AppointID)
);