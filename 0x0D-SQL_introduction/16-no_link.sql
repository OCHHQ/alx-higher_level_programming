-- Script to list all records with a name value in second_table, ordered by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
