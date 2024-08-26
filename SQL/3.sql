--3. We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?

SELECT DISTINCT wines.winery_id, wines.ratings_count, wines.name  AS wineries_name, wines.ratings_average FROM wines
INNER JOIN wineries ON wineries.name = wines.name
INNER JOIN vintages ON wines.id = vintages.wine_id
WHERE wines.ratings_average > 4.6 AND wines.ratings_count > 41000
ORDER BY wines.ratings_average DESC, wines.ratings_count DESC
LIMIT 3;






