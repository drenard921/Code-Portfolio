SELECT DISTINCT F.origin_city AS city
FROM FLIGHTS as F
WHERE 180 > ALL (SELECT F1.actual_time 
                 FROM FLIGHTS AS F1
				 WHERE F1.canceled = 0 AND
                       F.origin_city = F1.origin_city)
GROUP BY F.origin_city
ORDER BY city ASC;

/*
109 rows

Total execution time: 00:00:07.429

First 20 Entries:

Aberdeen SD
Abilene TX
Alpena MI
Ashland WV
Augusta GA
Barrow AK
Beaumont/Port Arthur TX
Bemidji MN
Bethel AK
Binghamton NY
Brainerd MN
Bristol/Johnson City/Kingsport TN
Butte MT
Carlsbad CA
Casper WY
Cedar City UT
Chico CA
College Station/Bryan TX
Columbia MO
Columbus GA
*/