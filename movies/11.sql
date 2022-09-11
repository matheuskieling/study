SELECT title FROM movies, stars, people, ratings
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND movies.id = ratings.movie_id
AND people.name LIKE 'Chadwick Boseman'
ORDER BY ratings.rating DESC
LIMIT 5;