--6. We would like to create a country leaderboard. Come up with a visual that shows the average wine rating for each country. Do the same for the vintages.
--wines
SELECT 
    wines.ratings_average,
    regions.country_code, 
    countries.name AS country_name
FROM 
    wines
INNER JOIN 
    regions ON regions.id = wines.region_id
INNER JOIN 
    countries ON regions.country_code = countries.code;


--vintages


WITH X AS (
    SELECT
        vintages.ratings_average,
        vintages.wine_id
    FROM
        vintages
    INNER JOIN wines ON vintages.wine_id = wines.id
)

SELECT 
    countries.name AS country_name,
    regions.country_code, 
    X.ratings_average
FROM
    X
INNER JOIN
    wines ON X.wine_id = wines.id
INNER JOIN
    regions ON regions.id = wines.region_id
INNER JOIN
    countries ON regions.country_code = countries.code
GROUP BY
    countries.name, regions.country_code
ORDER BY
    X.ratings_average DESC;
