SELECT SUM(F.capacity) as capacity
FROM MONTHS AS M, FLIGHTS AS F
WHERE M.mid = F.month_id AND
      M.month = "July" AND
      F.day_of_month = 10 AND
      ((F.origin_city = "Seattle WA" AND F.dest_city = "San Francisco CA") OR
      (F.origin_city = "San Francisco CA" AND F.dest_city = "Seattle WA"));

/*
1 row
*/