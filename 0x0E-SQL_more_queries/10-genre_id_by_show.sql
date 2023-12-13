-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select tv_shows.title and tv_show_genres.genre_id from relevant tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
