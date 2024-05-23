-- Script to list all records with a score >= 10 in second_table ordered by score (top first)

-- Select score and name from second_table where score is >= 10 ordered by score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
