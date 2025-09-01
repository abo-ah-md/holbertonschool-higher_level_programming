-- this is sub querry using forign key
SELECT 
    cities.id AS id,
    cities.name AS name,
    states.name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

