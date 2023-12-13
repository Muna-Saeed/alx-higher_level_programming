---

# 0x0E-SQL_more_queries

## Tasks

### 0. My privileges!
**Mandatory**

Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

```bash
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'

guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 

guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 

guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
```

### 1. Root user
**Mandatory**

Write a script that creates the MySQL server user user_0d_1.

```bash
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
```

### 2. Read user
**Mandatory**

Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

```bash
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
```

### 3. Always a name
**Mandatory**

Write a script that creates the table force_name on your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
```

### 4. ID can't be null
**Mandatory**

Write a script that creates the table id_not_null on your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
```

### 5. Unique ID
**Mandatory**

Write a script that creates the table unique_id on your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
```

### 6. States table
**Mandatory**

Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
```

### 7. Cities table
**Mandatory**

Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

```bash
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
```

### 8. Cities of California
**Mandatory**

Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

```bash
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah

guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas

guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   San Francisco
2   San Jose
```

### 9. Cities by States
**Mandatory**

Write a script that lists all cities contained in the database hbtn_0d_usa.

```bash
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name
1   California
2   Arizona
3   Texas
4   Utah

guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas

guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
```

### 10. Genre ID by show
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

```bash
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   

 7
House   8
House   10
House   11

```

### 11. Genre ID for all shows
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that lists all shows contained in hbtn_0d_tvshows.

```bash
guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
Breaking Bad
Dexter
Game of Thrones
House
```

### 12. No genre
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

```bash
guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
Dexter
House
```

### 13. Number of shows by genre
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

```bash
guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name    COUNT(title)
Crime   4
Drama   2
Mistery 2
Horror  1
Thriller    1
Fantasy 1
Comedy  1
Action  1
Family  1
```

### 14. My genre
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that uses the hbtn_0d_tvshows database to list all genres of Breaking Bad.

```bash
guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
name
Crime
Drama
Mistery
Thriller
```

### 15. Only Comedy
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that uses the hbtn_0d_tvshows database to list all Comedy shows.

```bash
guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title
Game of Thrones
```

### 16. List shows and genres
**Mandatory**

Import the database dump from hbtn_0d_tvshows to your MySQL server.

Write a script that uses the hbtn_0d_tvshows database to list all shows and their genre.

```bash
guillaume@ubuntu:~/$ cat 16-shows_and_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   name
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Mistery
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mistery
Dexter  Thriller
Game of Thrones Crime
Game of Thrones Fantasy
Game of Thrones Mistery
House   Crime
House   Mistery
House   Thriller
House   Comedy
House   Drama
```

---
