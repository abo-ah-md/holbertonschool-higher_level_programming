-- this to filter table in  the db in the server
SELECT score,name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;