SELECT DISTINCT C.name AS carrier
FROM CARRIERS AS C, FLIGHTS AS F
WHERE C.cid = F.carrier_id AND
	  F.origin_city = 'Seattle WA' AND
	  F.dest_city = 'San Francisco CA'
ORDER BY C.name ASC;


/*
4 rows

Total execution time: 00:00:01.987

Total Output: 

Alaska Airlines Inc.
SkyWest Airlines Inc.
United Air Lines Inc.
Virgin America
*/