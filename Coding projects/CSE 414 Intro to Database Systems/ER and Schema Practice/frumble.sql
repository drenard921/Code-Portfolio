/* initial table creation/import */
CREATE TABLE FRUMBLES (
    name VARCHAR(7),
    discount VARCHAR(3),
    month VARCHAR(3),
    price INT
);

/* importing txt */
.mode tab
.import mrFrumbleData.txt FRUMBLES

/* FD 1 */
/* name -> price */
SELECT COUNT(*)
FROM FRUMBLES AS F1, FRUMBLES AS F2
WHERE (F1.name = F2.name)
AND (F1.price != F2.price);
/* 
From lecture we know that if we don't see any entries 
the FD holds between name -> price
# of rows as output for this test was 0.
*/ 

/* FD 2 */
/* month -> discount  */ 
SELECT COUNT(*)
FROM FRUMBLES AS F1, FRUMBLES AS F2
WHERE (F1.month = F2.month)
AND (F1.discount != F2.discount);
/*
From lecture we know that if we don't see any entries
the FD holds between month -> discount
# of rows as output for this test was 0.
*/

/* One SQL test that didn't work */
/* discount <- month was not an FD */
SELECT COUNT(*)
FROM FRUMBLES AS F1, FRUMBLES AS F2
WHERE (F1.discount = F2.discount)
AND (F1.month != F2.month);


/* first BCNF Table */
CREATE TABLE R1 (
    name VARCHAR(110) PRIMARY KEY,
    price int
);

/* second BCNF Table */
CREATE TABLE R2 (
    month VARCHAR(3) PRIMARY KEY,
    discount VARCHAR(3)
);

/* third BCNF Table */
CREATE TABLE R3 (
    name VARCHAR(110) REFERENCES R1,
    month VARCHAR(3) REFERENCES R2
);


/* Importing data into our new tables */
INSERT OR IGNORE INTO R1 (name, price)
SELECT F.name, F.price 
FROM FRUMBLES AS F;

INSERT OR IGNORE INTO R2 (month, discount)
SELECT month, discount
FROM FRUMBLES AS F;

INSERT INTO R3 (name, month)
SELECT name, month
FROM FRUMBLES AS F;


/* Counting expected output */

SELECT COUNT(*) FROM R1;
/* R1 count: 36 rows */

SELECT COUNT(*) FROM R1;
/* R2 count: 12 rows  */

SELECT COUNT(*) FROM R1;
/* R3 count: 426 rows */
