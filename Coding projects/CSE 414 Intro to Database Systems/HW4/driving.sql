
CREATE TABLE Person (
    SSN INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE InsuranceCo (
    name VARCHAR(50) PRIMARY KEY, 
    phone VARCHAR(10)
);

CREATE TABLE Vehicle (
    licensePlate VARCHAR(7) PRIMARY KEY,
    year VARCHAR(4),
    SSN INT FOREIGN KEY REFERENCES Person, 
    name VARCHAR(50) REFERENCES Insurance,
    maxLiability INT
);

CREATE TABLE Car (
    licensePlate VARCHAR(7) PRIMARY KEY REFERENCES Vehicle,
    make VARCHAR(25),
    SSN INT REFERENCES Person
);

CREATE TABLE Truck (
    licensePlate VARCHAR(7) PRIMARY KEY REFERENCES Vehicle,
    capacity INT,
    SSN INT REFERENCES Person
);

CREATE TABLE Driver( 
    SSN INT PRIMARY KEY REFERENCES Person,
    driverID INT
);

CREATE TABLE NonProfessionalDriver(
    SSN INT PRIMARY KEY REFERENCES Driver
);

CREATE TABLE ProfessionalDriver(
    SSN INT PRIMARY KEY REFERENCES Driver,
    medicalHistory VARCHAR(150)
);


/*

P2 part b:
Logically,
each vehicle might have its own maxLiability, 
a given vehicle will only be covered by a single insurance company at a time,
but many vehicles have insurance.

for these reasons: 
The relation in my relational schema that represents the relationship "insures" is 
the foreign key reference in the Vehicle table to the "name" field 
from the InsuranceCo table. 
Also in the Vehicle table I've also added a maxliability field.
This way many vehicles with a maxLiability can be linked 
to a there single InsuranceCompany by that company's name
to support this relationship of insurance.

P2 part c:

Drives seems to be optimized to keep track of all the different relationships 
of car(s) being driven by one or more non-professional drivers. 
Which makes sense if you want to know who's driving which vehicles. 

Operates seems to be optimized to keep track of which trucks 
are being driven by a given professional driver in a given trip and 
whether or not that professional driver is healthy.
This information would be important to keep track of trips
where a a company truck might be operated by an employee.

Differences:
Drives is a many to many relationship whereas Operates is a many to one relationship 
this is the main difference between the two.

To explain why each relationship is the way it is:
Drives is a many to many relationship. Such that a non-professional driver can drive many cars
which makes sense because a non-professional driver might own and drive several cars and 
in another case, multipe non-professional drivers in the same household might operate 
the same cars. To support both cases this is why Drives is a many to many relationship.

Operates on the otherhand is different because it has a many to one relationship. 
Such that many trucks can be operated by a given professional driver 
but a single truck can only be operated by one professional driver at a time.

*/