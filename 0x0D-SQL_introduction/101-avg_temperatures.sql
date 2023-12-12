-- Task: Average Temperatures by City
-- This script displays the average temperature (in Fahrenheit) by city, ordered by temperature in descending order.

SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
