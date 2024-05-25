--
-- 16-shows_by_genre.sql
--
-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
--

SELECT 
    ts.title, g.name
FROM 
    tv_shows ts
LEFT JOIN 
    tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN 
    tv_genres g ON tsg.genre_id = g.id
ORDER BY 
    ts.title ASC, g.name ASC;
