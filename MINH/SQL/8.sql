
--Question 8: What is the distribution of wines across different taste profiles (e.g., sweetness, acidity, tannin), and how do these profiles correlate with ratings?


SELECT 
    keywords.name AS wines_taste,
    ROUND(AVG(wines.ratings_average), 1) AS avg_ratings_average,
    ROUND(AVG(wines.acidity), 2) AS avg_acidity,
    ROUND(AVG(wines.intensity), 2) AS avg_intensity,
    ROUND(AVG(wines.sweetness), 2) AS avg_sweetness,
    ROUND(AVG(wines.tannin), 2) AS avg_tannin

FROM wines
INNER JOIN keywords_wine ON wines.id = keywords_wine.wine_id
INNER JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE wines.acidity IS NOT NULL
AND wines.intensity IS NOT NULL
AND wines.sweetness IS NOT NULL
AND wines.tannin IS NOT NULL
AND wines.ratings_average IS NOT NULL
GROUP BY keywords.name
ORDER BY avg_ratings_average DESC;


