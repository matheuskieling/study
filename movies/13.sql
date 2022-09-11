SELECT DISTINCT(name) from people, stars, movies
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND movies.title IN(SELECT DISTINCT(title) from people, stars, movies
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND name = "Kevin Bacon"
AND birth = 1958)
AND name NOT IN("Kevin Bacon");