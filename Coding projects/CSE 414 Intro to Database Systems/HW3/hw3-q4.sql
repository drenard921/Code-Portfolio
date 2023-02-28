SELECT DISTINCT F2.dest_city AS city
FROM FLIGHTS AS F1, FLIGHTS AS F2
WHERE F1.origin_city = 'Seattle WA' AND 
      F2.dest_city NOT IN (SELECT F3.dest_city
	  					   FROM FLIGHTS AS F3
						   WHERE F3.origin_city = 'Seattle WA') AND
	  F2.origin_city = F1.dest_city AND 
      F2.dest_city <> 'Seattle WA'
ORDER BY city ASC;

/*
256 rows

Total execution time: 00:00:13.105

First 20 Entries:

Aberdeen SD
Abilene TX
Adak Island AK
Aguadilla PR
Akron OH
Albany GA
Albany NY
Alexandria LA
Allentown/Bethlehem/Easton PA
Alpena MI
Amarillo TX
Appleton WI
Arcata/Eureka CA
Asheville NC
Ashland WV
Aspen CO
Atlantic City NJ
Augusta GA
Bakersfield CA
Bangor ME
*/