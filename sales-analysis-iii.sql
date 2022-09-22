# Write your MySQL query statement below
SELECT p_id AS product_id, product_name
FROM (SELECT product_id AS p_id
      FROM Sales
      GROUP BY product_id
      HAVING 
        (MAX(sale_date) BETWEEN "2019-01-01" AND "2019-03-31") AND 
        MIN(sale_date) BETWEEN "2019-01-01" AND "2019-03-31") AS temp
LEFT JOIN Product
ON Product.product_id = temp.p_id;


