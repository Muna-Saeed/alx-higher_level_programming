-- Task: Number of Shows by Genre
-- This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each.

SELECT tv_show_genres.genre AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;
