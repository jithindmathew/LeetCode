SELECT 
    *,
    IF(x+y > z AND x+z > y AND y+z > x) AS triangle
FROM
    triangle;