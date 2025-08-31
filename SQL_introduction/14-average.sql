-- this to filter table in  the db in the server
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;