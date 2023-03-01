CAR(car_id primary key, Serial_Number, Model_No, Color, Year, Customer_ID Foreign key, Emp_ID Foreign key)

CUSTOMER(Customer_ID primary key, Name, PhoneNumber, Address, Country, City)

EMPLOYEE(EmpID primary key, Name Address,)

EMPLOYEE_QUALIFICATION(EmpID primary key, Qualification primary key)

INVOICE(InvoiceID primary key, Date, CustomerID Foreign Key, EmpID Foreign Key)