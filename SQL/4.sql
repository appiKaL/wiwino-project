--4. We detected that a big cluster of customers likes a specific combination of tastes. We identified a few keywords that match these tastes: coffee, toast, green apple, cream, and citrus (note that these keywords are case sensitive ⚠️). We would like you to find all the wines that are related to these keywords. Check that at least 10 users confirm those keywords, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.



SELECT wines.name AS wines_name,keywords.name AS keywords_name,keywords_wine.group_name
FROM wines
INNER JOIN keywords_wine ON wines.id = keywords_wine.wine_id
INNER JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE ( keywords.name LIKE '%coffee%' OR keywords.name LIKE '%toast%' OR keywords.name LIKE '%green apple%' OR keywords.name LIKE '%cream%' OR keywords.name LIKE '%citrus%' ) AND ( wines_name IS NOT NULL OR keywords_name IS NOT NULL OR group_name IS NOT NULL )
ORDER BY wines.name, keywords.name, keywords_wine.group_name;



