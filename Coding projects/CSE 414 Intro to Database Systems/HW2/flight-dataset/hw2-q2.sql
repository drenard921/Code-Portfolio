SELECT 
       F1.flight_num AS f1_flight_num, 
       F1.origin_city AS f1_origin_city, 
       F1.dest_city AS f1_dest_city, 
       F1.actual_time AS f1_actual_time,
       F2.flight_num AS f2_flight_num,
       F2.origin_city AS f2_origin_city,
       F2.dest_city AS f2_dest_city,
       F2.actual_time AS f2_actual_time,
       (F1.actual_time + F2.actual_time) AS actual_time
FROM FLIGHTS AS F1, FLIGHTS AS F2, MONTHS AS M, CARRIERS AS C
WHERE
    C.cid = F1.carrier_id AND
    F1.carrier_id = F2.carrier_id AND
    F1.month_id = F2.month_id AND
    M.mid = F1.month_id AND
    M.month = 'July' AND
    F1.day_of_month = F2.day_of_month AND
    F2.day_of_month = 15 AND
    f1_origin_city = 'Seattle WA' AND 
    f2_origin_city = f1_dest_city AND 
    f2_dest_city = 'Boston MA' AND
    (F1.actual_time + F2.actual_time)/60 < 7;

/*
1472 rows
*/