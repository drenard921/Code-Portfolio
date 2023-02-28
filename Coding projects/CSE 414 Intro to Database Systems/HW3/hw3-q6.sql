SELECT DISTINCT C.name
FROM CARRIERS AS C
WHERE C.cid IN (SELECT F.carrier_id 
 			    FROM FLIGHTS AS F
 			    WHERE F.origin_city = 'Seattle WA' AND
	                  F.dest_city = 'San Francisco CA')
ORDER BY C.name ASC;


/*
4 rows

Total execution time: 00:00:02.460

Total Output:

Alaska Airlines Inc.
SkyWest Airlines Inc.
United Air Lines Inc.
Virgin America
*/