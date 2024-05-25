-- Select all cities with their respective states
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;