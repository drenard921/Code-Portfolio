SELECT DISTINCT F1.dest_city AS city
FROM FLIGHTS AS F1
WHERE F1.dest_city NOT IN (SELECT F2.dest_city
	  					         FROM FLIGHTS AS F2
						         WHERE F2.origin_city = 'Seattle WA') AND
	  F1.dest_city NOT IN (SELECT F4.dest_city
									FROM FLIGHTS AS F3, FLIGHTS AS F4
									WHERE F3.origin_city = 'Seattle WA' AND
	  										F4.origin_city = F3.dest_city)
ORDER BY city ASC;
/*
3 rows 

Total execution time: 00:03:42.241

Total Output:

Devils Lake ND
Hattiesburg/Laurel MS
St. Augustine FL
*/