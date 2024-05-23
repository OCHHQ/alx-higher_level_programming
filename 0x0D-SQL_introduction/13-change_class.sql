-- Script to remove all records with a score <= 5 in second_table

-- Delete records where the score is less than or equal to 5
DELETE FROM second_table
WHERE score <= 5;
