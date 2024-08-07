--
-- 11-genre_id_all_shows.sql
--
-- Lists all shows contained in the database hbtn_0d_tvshows.
--

SELECT 
    ts.title, tsg.genre_id
FROM 
    tv_shows ts
LEFT JOIN 
    tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY 
    ts.title ASC, tsg.genre_id ASC;
