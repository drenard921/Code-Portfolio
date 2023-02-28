SELECT C.name, Avg(F.canceled) * 100.0 AS percentage
FROM FLIGHTS AS F, CARRIERS AS C
WHERE C.cid = F.carrier_id AND
      F.origin_city = "Seattle WA"
GROUP BY C.cid
HAVING percentage > 0.5
ORDER BY percentage;

/* 
6 rows
*/