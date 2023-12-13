-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select the id of the state named California
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- Select all cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_id
ORDER BY cities.id ASC;
