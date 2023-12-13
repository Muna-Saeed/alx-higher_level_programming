-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select cities.id, cities.name, and states.name and join cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
