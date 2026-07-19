SELECT item, SUM(total_spent) AS revenue
FROM cafe_sales
GROUP BY item
ORDER BY revenue DESC;

SELECT month, SUM(total_spent) AS revenue
FROM cafe_sales
GROUP BY month;

SELECT payment_method, COUNT(*)
FROM cafe_sales
GROUP BY payment_method;

SELECT location, SUM(total_spent)
FROM cafe_sales
GROUP BY location;

SELECT item, COUNT(*)
FROM cafe_sales
GROUP BY item
ORDER BY COUNT(*) DESC;






