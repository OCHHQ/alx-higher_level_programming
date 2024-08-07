--
-- 13-count_shows_by_genre.sql
--
-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
--

SELECT 
    g.name AS genre, 
    COUNT(tsg.show_id) AS number_of_shows
FROM 
    tv_genres g
LEFT JOIN 
    tv_show_genres tsg ON g.id = tsg.genre_id
GROUP BY 
    g.name
HAVING 
    COUNT(tsg.show_id) > 0
ORDER BY 
    number_of_shows DESC;
