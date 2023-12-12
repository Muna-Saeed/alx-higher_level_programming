-- Import the table dump into the hbtn_0c_0 database
USE hbtn_0c_0;

-- Source the table dump file (adjust the path accordingly)
SOURCE /path/to/your/table_dump_file.sql;

-- Query to display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
