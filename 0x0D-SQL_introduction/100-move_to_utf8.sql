-- Convert hbtn_0c_0 database to UTF8
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
USE hbtn_0c_0;

-- Convert the first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
