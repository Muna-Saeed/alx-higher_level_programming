-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- List all shows by their rating
SELECT tv_shows.title, SUM(tv_shows_rate.rating) as rating_sum
FROM tv_shows
LEFT JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
