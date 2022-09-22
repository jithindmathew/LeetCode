# Write your MySQL query statement below

WITH temp AS (
    SELECT
        Department.name AS "Department",
        Employee.name AS "Employee",
        Employee.salary AS "Salary",
        RANK() OVER(PARTITION BY Department.name ORDER BY Employee.salary DESC) AS "rank"
    FROM Employee
    LEFT JOIN Department
    ON Employee.departmentId = Department.id
    ORDER BY Department.name
)

SELECT Department, Employee, Salary
FROM temp
WHERE temp.rank = 1;
