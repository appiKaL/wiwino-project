--7. One of our VIP clients likes Cabernet Sauvignon and would like our top 5 recommendations. Which wines would you recommend to him?


SELECT wines.name AS wines_names, wines.ratings_average,wines.ratings_count

FROM wines

WHERE wines.name LIKE '%Cabernet Sauvignon%' AND ( wines.name IS NOT NULL OR wines.ratings_average IS NOT NULL OR wines.ratings_count IS NOT NULL ) AND wines.ratings_count > 1300 AND wines.ratings_average > 4.4
ORDER BY wines.ratings_average DESC, wines.ratings_count DESC

LIMIT 5;
