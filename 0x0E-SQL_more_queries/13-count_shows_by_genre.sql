-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(show_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres
ON genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
