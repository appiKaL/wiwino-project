

--2. We have a limited marketing budget for this year. Which country should we prioritise and why?

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
