--1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?


SELECT wines.name,wines.ratings_average,wines.ratings_count
FROM wines
WHERE wines.ratings_count > 20000 AND wines.ratings_average >= 4.6
ORDER BY wines.ratings_average DESC , wines.ratings_count DESC
LIMIT 10;

