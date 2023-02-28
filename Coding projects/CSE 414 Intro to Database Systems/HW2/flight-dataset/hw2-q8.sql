SELECT C.name as name, SUM(F.departure_delay) as delay 
FROM FLIGHTS AS F, CARRIERS AS C
WHERE C.cid = F.carrier_id
GROUP BY C.name;

/* 
22 rows
*/ 