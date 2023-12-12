-- Convert hbtn_0c_0 database to UTF8
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 

-- Convert the first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Update the collation of the name field in first_table
ALTER TABLE first_table MODIFY COLUMN name varchar(256) COLLATE utf8mb4_unicode_ci;

-- Convert the default character set and collation of the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
