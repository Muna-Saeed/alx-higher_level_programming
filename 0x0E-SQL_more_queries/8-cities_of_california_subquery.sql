-- Task: List Cities of California
-- This script lists all the cities of California from the hbtn_0d_usa database.

-- Select the id of the California state from the states table
SELECT id FROM states WHERE name = 'California' INTO @california_state_id;

-- Select the cities of California based on the state_id in the cities table
SELECT id, name FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
