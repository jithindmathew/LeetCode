# Write your MySQL query statement below
SELECT name, balance 
FROM (SELECT account, SUM(AMOUNT) AS balance
      FROM Transactions
      GROUP BY account
      HAVING balance > 10000) AS temp
LEFT JOIN Users
ON Users.account = temp.account;