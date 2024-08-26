

-- 1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?

WITH CombinedData AS (
    SELECT
        w.id AS wine_id,
        w.name AS wine_name,
        w.ratings_average AS wine_rating_average,
        w.ratings_count AS wine_rating_count,
        v.year AS vintage_year,
        v.ratings_average AS vintage_rating_average,
        v.ratings_count AS vintage_rating_count
    FROM
        wines w
    INNER JOIN
        vintages v ON w.id = v.wine_id
),
WeightedAverage AS (
    SELECT
        wine_id,
        wine_name,
        -- Ağırlıklı ortalamayı hesapla
        SUM(vintage_rating_average * vintage_rating_count) / NULLIF(SUM(vintage_rating_count), 0) AS weighted_average
    FROM
        CombinedData
    GROUP BY
        wine_id, wine_name
),
WineYear AS (
    SELECT
        w.wine_id,
        w.wine_name,
        w.weighted_average,
        v.vintage_year
    FROM
        WeightedAverage w
    INNER JOIN
        CombinedData v ON w.wine_id = v.wine_id
    WHERE
        v.vintage_year = (SELECT MAX(vintage_year) FROM CombinedData WHERE wine_id = w.wine_id)
)
SELECT
    wine_id,
    wine_name,
    weighted_average,
    vintage_year
FROM
    WineYear
ORDER BY

    weighted_average DESC,
    vintage_year DESC
    
LIMIT 10;




-- 2. We have a limited marketing budget for this year. Which country should we prioritise and why?


WITH country_data AS (
    SELECT
        c.name AS country_name,
        c.wineries_count,
        c.users_count,
        CASE
            WHEN c.users_count IS NOT NULL AND c.users_count <> 0 THEN c.users_count
            ELSE 0
        END AS wines_per_user,
        COALESCE(COUNT(t.name), 0) AS toplists_count
    FROM
        countries c
    LEFT JOIN
        toplists t ON c.code = t.country_code
    GROUP BY
        c.name, c.wineries_count, c.users_count
)

SELECT
    country_name,
    wineries_count,
    wines_per_user,
    toplists_count
FROM
    country_data
ORDER BY
    toplists_count DESC,       -- Prioritize by number of toplist appearances
    wines_per_user DESC,       -- Then by wines per user
    wineries_count DESC        -- Finally by number of wineries
LIMIT 5;                      -- Retrieve only the top 5 records




