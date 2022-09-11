SELECT DISTINCT(title) from people, stars, movies
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = 'Johnny Depp'
INTERSECT
SELECT DISTINCT(title) from people, stars, movies
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = 'Helena Bonham Carter';
