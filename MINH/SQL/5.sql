
--5. We would like to select wines that are easy to find all over the world. Find the top 3 most common grapes all over the world and for each grape, give us the the 5 best rated wines.


-- most common grapes all over the world

SELECT grapes.name AS grape_name
FROM most_used_grapes_per_country
INNER JOIN grapes ON most_used_grapes_per_country.grape_id = grapes.id  
GROUP BY grapes.name
ORDER BY COUNT(*) DESC
LIMIT 3;

--Cabernet Sauvignon

SELECT name, ratings_average, ratings_count
FROM wines
WHERE name LIKE '%Cabernet Sauvignon%'

AND ratings_average > 4.5
AND ratings_count > 2500
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;



--Merlot

SELECT name, wines.ratings_average, wines.ratings_count
FROM wines
WHERE (wines.name LIKE '%Merlot%')
ORDER BY wines.ratings_average DESC, wines.ratings_count DESC
LIMIT 5;


--Chardonnay
SELECT name, ratings_average, ratings_count
FROM wines
WHERE name LIKE '%Chardonnay%'
AND ratings_average >= 4.3

ORDER BY ratings_average DESC, ratings_count DESC, name
LIMIT 5;
