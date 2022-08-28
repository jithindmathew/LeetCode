# Write your MySQL query statement below
# SELECT name
# FROM Users;
SELECT name, IF (travelled_distance IS NULL, 0, travelled_distance) AS travelled_distance 
FROM Users LEFT JOIN (SELECT user_id, SUM(distance) AS travelled_distance 
                      FROM Rides 
                      GROUP BY user_id) AS temp
ON Users.id = temp.user_id
ORDER BY travelled_distance DESC, name;