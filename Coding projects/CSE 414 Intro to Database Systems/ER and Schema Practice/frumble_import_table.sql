.mode tab
.import mrFrumbleData.txt FRUMBLES




/* Importing into tables */
INSERT OR IGNORE INTO R1 (name, price)
SELECT F.name, F.price 
FROM FRUMBLES AS F;

INSERT OR IGNORE INTO R2 (month, discount)
SELECT month, discount
FROM FRUMBLES AS F;

INSERT INTO R3 (name, month)
SELECT name, month
FROM FRUMBLES AS F;