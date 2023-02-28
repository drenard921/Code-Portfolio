SELECT W.day_of_week, Avg(F.departure_delay) AS delay
FROM FLIGHTS AS F, WEEKDAYS AS W
WHERE 
    F.day_of_week_id = W.did
GROUP BY W.did, W.day_of_week
ORDER BY delay DESC
LIMIT 1; 

/*
1 row
*/