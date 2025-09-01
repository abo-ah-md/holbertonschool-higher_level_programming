-- this is sub querry using forign key
SELECT 
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id)
FROM tv_show_genres
JOIN  genre
    ON tv_genres = tv_show_genres.genre_id
    GROUP BY  tv_genres.name
ORDER BY genres.name ASC;