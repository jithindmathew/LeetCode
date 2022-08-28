# Write your MySQL query statement below
SELECT product_id, 'store1' as store, store1 as price
FROM Products
WHERE store1 iS NOT NULL

UNION

SELECT product_id, 'store2' as store, store2 as price
FROM Products
WHERE store2 iS NOT NULL

UNION

SELECT product_id, 'store3' as store, store3 as price
FROM Products
WHERE store3 iS NOT NULL

ORDER BY product_id, store;