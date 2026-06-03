-- Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Total transactions
SELECT COUNT(*)
FROM fact_transactions;

-- Average transaction amount
SELECT AVG(amount)
FROM fact_transactions;

-- Funds with expense ratio below 1
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Maximum NAV
SELECT MAX(nav)
FROM fact_nav;

-- Minimum NAV
SELECT MIN(nav)
FROM fact_nav;

-- Total AUM
SELECT SUM(aum)
FROM fact_aum;

-- Transaction types
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Average expense ratio
SELECT AVG(expense_ratio)
FROM fact_performance;