-- this is sub querry using forign key
SELECT cities.id, cities.name, states.name FROM cities 
JOIN states ON cities.state.id = state_id
ORDER BY ASC;

