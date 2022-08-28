# # Write your MySQL query statement below
# SELECT
#     class
# FROM
#     (SELECT
#         class, COUNT(DISTINCT student) AS num
#     FROM
#         Courses
#     GROUP BY
#         class) AS temp
# WHERE
#     num >5; 

SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;