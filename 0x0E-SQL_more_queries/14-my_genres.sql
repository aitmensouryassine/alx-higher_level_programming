-- lists all genres of the show Dexter.

SELECT tv_genres.name FROM tv_show_genres
       INNER JOIN tv_genres
       ON tv_genres.id = genre_id
       INNER JOIN tv_shows
       ON show_id = tv_shows.id
       WHERE tv_shows.title = "Dexter"
       ORDER BY tv_genres.name;
