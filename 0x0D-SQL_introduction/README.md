# SQL Introduction Project

This project focuses on learning and applying various SQL concepts using MySQL. Below are the tasks and corresponding scripts:

## Task 0: List Databases
**Script:** [0-list_databases.sql](0x0D-SQL_introduction/0-list_databases.sql)
```sql
-- List all databases
SHOW DATABASES;
```

## Task 1: Create a Database if Missing
**Script:** [1-create_database_if_missing.sql](0x0D-SQL_introduction/1-create_database_if_missing.sql)
```sql
-- Create hbtn_0c_0 database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

## Task 2: Delete a Database
**Script:** [2-remove_database.sql](0x0D-SQL_introduction/2-remove_database.sql)
```sql
-- Delete hbtn_0c_0 database if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;
```

## Task 3: List Tables
**Script:** [3-list_tables.sql](0x0D-SQL_introduction/3-list_tables.sql)
```sql
-- List all tables in the given database
SHOW TABLES FROM hbtn_0c_0;
```

## Task 4: First Table
**Script:** [4-first_table.sql](0x0D-SQL_introduction/4-first_table.sql)
```sql
-- Create or alter the first_table
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(256)
);
```

## Task 5: Full Description
**Script:** [5-full_table.sql](0x0D-SQL_introduction/5-full_table.sql)
```sql
-- Display full description of first_table
DESCRIBE hbtn_0c_0.first_table;
```

## Task 6: List All in Table
**Script:** [6-list_values.sql](0x0D-SQL_introduction/6-list_values.sql)
```sql
-- List all rows of first_table
SELECT * FROM hbtn_0c_0.first_table;
```

## Task 7: First Add
**Script:** [7-insert_value.sql](0x0D-SQL_introduction/7-insert_value.sql)
```sql
-- Insert a new row into first_table
INSERT INTO hbtn_0c_0.first_table (id, name) VALUES (89, 'Best School');
```

## Task 8: Count 89
**Script:** [8-count_89.sql](0x0D-SQL_introduction/8-count_89.sql)
```sql
-- Display the count of records with id = 89 in first_table
SELECT COUNT(*) FROM hbtn_0c_0.first_table WHERE id = 89;
```

## Task 9: Full Creation
**Script:** [9-full_creation.sql](0x0D-SQL_introduction/9-full_creation.sql)
```sql
-- Create or alter second_table and add multiple rows
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);

INSERT INTO second_table VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
```

## Task 10: List by Best
**Script:** [10-top_score.sql](0x0D-SQL_introduction/10-top_score.sql)
```sql
-- List all records of second_table ordered by score (top first)
SELECT * FROM hbtn_0c_0.second_table ORDER BY score DESC;
```

## Task 11: Select the Best
**Script:** [11-best_score.sql](0x0D-SQL_introduction/11-best_score.sql)
```sql
-- List records with score >= 10 in second_table ordered by score (top first)
SELECT * FROM hbtn_0c_0.second_table WHERE score >= 10 ORDER BY score DESC;
```

## Task 12: Cheating is Bad
**Script:** [12-no_cheating.sql](0x0D-SQL_introduction/12-no_cheating.sql)
```sql
-- Update the score of Bob to 10 in second_table without using Bob's id
UPDATE hbtn_0c_0.second_table SET score = 10 WHERE name = 'Bob';
```

## Task 13: Score Too Low
**Script:** [13-change_class.sql](0x0D-SQL_introduction/13-change_class.sql)
```sql
-- Remove all records with score <= 5 in second_table
DELETE FROM hbtn_0c_0.second_table WHERE score <= 5;
```

## Task 14: Average
**Script:** [14-average.sql](0x0D-SQL_introduction/14-average.sql)
```sql
-- Compute the average score of all records in second_table
SELECT AVG(score) AS average FROM hbtn_0c_0.second_table;
```

## Task 15: Number by Score
**Script:** [15-groups.sql](0x0D-SQL_introduction/15-groups.sql)
```sql
-- List the number of records for each score in second_table, ordered by the number of records (descending)
SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC;
```

## Task 16: Say My Name
**Script:** [16-no_link.sql](0x0D-SQL_introduction/16-no_link.sql)
```sql
-- List all records of second_table without rows without a name value, ordered by descending score
SELECT * FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;
```

## Task 17: Go to UTF8
**Script:** [100-move_to_utf8.sql](0x0D-SQL_introduction/100-move_to_utf8.sql)
```sql
-- Convert hbtn_0c_0 database, first_table, and name field to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Task 18: Temperatures #0
**Script:** [101-avg_temperatures.sql](0x0D-SQL_introduction/101-avg_temperatures.sql)
```sql
-- Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Data imported from provided dump
```

## Task 19: Temperatures #1
**Script:** [102-top_city.sql](0x0D-SQL_introduction/102-top_city.sql)
```sql
-- Display the top 3 cities' temperature during July and August ordered by temperature (descending)
-- Data imported from provided dump
```

## Task 20: Temperatures #2
**Script:** [103-max_state.sql](0x0D-SQL_introduction/

103-max_state.sql)
```sql
-- Display the max temperature of each state ordered by state name
-- Data imported from provided dump
```
