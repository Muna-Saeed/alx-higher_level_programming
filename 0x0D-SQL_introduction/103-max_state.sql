-- Task: Max Temperature by State
-- This script displays the maximum temperature of each state, ordered by state name.
-- cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
