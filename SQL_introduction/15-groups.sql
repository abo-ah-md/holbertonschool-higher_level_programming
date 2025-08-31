-- this to filter table in  the db in the server
SELECT score, count (*) AS number
FROM second_table
GROUP BY score
ORDER by DESC;