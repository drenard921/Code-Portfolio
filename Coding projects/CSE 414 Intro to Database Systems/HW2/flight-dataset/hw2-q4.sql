SELECT DISTINCT C.name
FROM FLIGHTS AS F, CARRIERS AS C
WHERE C.cid = F.carrier_id
GROUP BY C.cid, F.day_of_month, F.month_id
HAVING COUNT(F.fid) > 1000;

/*
12 rows
*/