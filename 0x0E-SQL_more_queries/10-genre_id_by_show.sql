--
-- 10-genre_id_by_show.sql
--
-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
--

SELECT 
    ts.title, tsg.genre_id
FROM 
    tv_shows ts
JOIN 
    tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY 
    ts.title ASC, tsg.genre_id ASC;
