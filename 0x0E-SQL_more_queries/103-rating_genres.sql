-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- List all genres by their rating
SELECT tv_genres.name, SUM(tv_shows_rate.rating) as rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
LEFT JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
