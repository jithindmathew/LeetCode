# Write your MySQL query statement below
SELECT
    customers.name AS 'Customers'
FROM
    Customers
WHERE
    Customers.id NOT IN (
            SELECT
                customerid
            FROM
                orders
    );
