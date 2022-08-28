# Write your MySQL query statement below
SELECT
    w2.id
FROM
    weather W1 JOIN weather w2 
        ON DATEDIFF(w1.recorddate, w2.recorddate) = -1
WHERE
    w2.temperature > w1.temperature;