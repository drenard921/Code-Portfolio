SELECT DISTINCT F.flight_num
FROM FLIGHTS AS F, WEEKDAYS AS W, CARRIERS AS C
WHERE
      F.carrier_id = C.cid AND
      F.day_of_week_id = W.did AND
      C.name = 'Alaska Airlines Inc.' AND
      W.day_of_week = 'Monday' AND
      F.origin_city = 'Seattle WA' AND
      F.dest_city = 'Boston MA';

/* 
3 rows
*/