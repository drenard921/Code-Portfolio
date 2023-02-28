/*
Dylan Renard 
10/06/21
CSE 414 
Ryan Maas
*/

/*
HW #1 SQLite3 intro: 
In HW #1 We went over the basics of
    * Table Creation
    * Data Insertion
    * Data Type convention
    * Data recall
    * Basic SQL search queries
*/

/*
Q2.1 (create table)
    Create a table Edges(Source, Destination) 
    where both Source and Destinations are integers.
*/

CREATE TABLE Edges (Source INT, Destination INT);

/*
Q2.2 (data entry)
    In Edges table, 
    Insert:
    (10,5), (6,25), (1,3), (4,4).
*/

INSERT INTO Edges VALUES (10,5), (6,25), (1,3), (4,4);


/* 
Q2.3 (simple data table query)
    Write SQL statement that returns all tuples.
*/

SELECT * FROM Edges;

/*
Q2.4 (column data table query)
    Write SQL statement that returns only column Source for all tuples.
*/
.header ON
.mode column 
SELECT E.Source
FROM Edges AS E;

/*
Q2.5 (data selection meeting condintion)
    Write SQL Statement that returns all tuples where,
    (INT) Source > (INT) Destination
*/
.header ON
.mode column
SELECT e.source, e.destination
FROM Edges e
WHERE e.source > e.destination;

/* QUESTION!!!
Q2.6 (negative data entry)
    Now insert tuple ('-1','2000').
    Might not work check documentation to add this value.
*/

    /* Side Note:
        Database is set up to take two INT parameters.
        Values passed in are currently TEXT types. 
        A resolution to this error, 
        is to cast the TEXT as INT when doing data entry.
    */


/* 
Type affinity: no need for casting 
SQL has (implicit data conversion)
*/

INSERT INTO Edges 
    VALUES ('-1', '2000');

/*
Q3 (create table with different data types)
    myRestaurants table specs:
    Table Attributes:
    * Name of the Restaurant: a varchar field
    * Distance (in minutes) from your house: an int
    * Date of your last visit: a varchar field, interpreted as date
    * Whether you liked it or not: an int, Interpreted as Boolean
*/

CREATE TABLE my_restaurants (
    restaurant_name VARCHAR(50),
    food_type VARCHAR (35),
    dist_home INT,
    last_visit VARCHAR(10),
    like_restaurant INT);

/*
Q4 (data entry into myRestaurants)
    Insert at least five tuples using the SQL INSERT command five (or more) times. 
    You should insert one restaurant you liked, at least one you did not like,
    and at least one restaurant where you leave "I like" field NULL.
*/

INSERT INTO my_restaurants
    VALUES ('Chi Mac', 'Korean BBQ', 25, '2021-10-02', 1),
            ('Agua Verde', 'Mexican', 10, '2021-10-01', 1),
            ("Alladin's Gyrocery", 'Mediteranean', 20, '2021-09-27',1),
            ("Dub Street Burger's (Local Point)", 'Fast-Food', 8, '2021-09-29', 0),
            ('Memos', 'Mexican', 30, '2020-01-27', 0),
            ('Nobu', 'Japanese Sushi', 22560, '2014-07-31', 0),
            ('Japonesa', 'Japanese Sushi', 40, '2020-08-14', 1);



/*
Q5.1 (data reporting)
    Turn column headers on, then output the results in these three formats:
    1. print the results in comma-separated form
    2. print the results in list form, delimited by "|"
    3. print the results in column form and make every column have width 15 
       (be sure that every column has width 15 and not just the first one)   
*/

/* turning header on */
.header ON

/* 5.1.1  CSV form */
.mode csv
SELECT * FROM my_restaurants;

/* 5.1.2 list form */
.mode list
SELECT * FROM my_restaurants;
/* 5.1.3 column form with width 15 */
.mode column
.width 15 15 15
SELECT * FROM my_restaurants;

/* 
Q5.2 (data reporting without headers)
    Turn column headers off, then output the results in these three formats:
    1. print the results in comma-separated form
    2. print the results in list form, delimited by "|"
    3. print the results in column form and make every column have width 15 
       (be sure that every column has width 15 and not just the first one)
*/

/* turning header off */
.header OFF

/* 5.2.1  CSV form */
.mode csv
Select * FROM my_restaurants;

/* 5.2.2 list form */
.mode list
SELECT * FROM my_restaurants;

/* 5.2.3 column form with width 15 */
.mode column
.width 15 15 15
SELECT * FROM my_restaurants;


/* 
Q6 (SQL querying)
    Write a SQL query that returns only the name and distance 
    of all restaurants within and including 20 minutes of your house. 
    The query should list the restaurants in alphabetical order of names.    
*/

SELECT r.restaurant_name, r.dist_home
FROM my_restaurants r
WHERE r.dist_home <= 20;
ORDER BY r.restaurant_name ASC

/*
Q7 (SQL date querying)
    Write a SQL query that returns all restaurants that you like, 
    but has not visited since more than 3 months ago. 
    Make sure that you use the date() function to calculate the date 3 months ago.
*/

SELECT * FROM my_restaurants 
WHERE like_restaurant == 1 AND 
      last_visit <  date('now', '-3 month');



/*
Q8 (SQL distance home querying)
    Write a SQL query that returns all restaurants that are 
    within and including 10 mins from your house.
*/

SELECT * FROM my_restaurants r 
WHERE r.dist_home <= 10;

