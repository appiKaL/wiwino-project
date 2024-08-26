import csv

import sqlite3 

connexion=sqlite3.connect('vivino.db')

cursor=connexion.cursor()


print("2. We have a limited marketing budget for this year. Which country should we prioritise and why?")

print(" the highest number of wineries by country")

query3 = """   
SELECT 
    wineries_count,
    countries.name
FROM
    countries
GROUP BY
    countries.name
ORDER BY
    wineries_count DESC
"""

cursor.execute(query3)
for row in cursor.fetchall():
    print(row)


print("----------------")





print("wines count by country")
query5 = """   
SELECT  DISTINCT
    wines_count,
    countries.name
FROM
    countries
GROUP BY
    countries.name
ORDER BY
    wines_count DESC
"""

cursor.execute(query5)
for row in cursor.fetchall():
    print(row)


print("----------------")

# number of wines count in each person by country
print("number of wines count in each person by country")
query4 = """
SELECT DISTINCT
    countries.name,
    wines_count,
    users_count
FROM 
    countries
    
GROUP BY
    countries.name
ORDER BY
    wines_count / users_count DESC
    

"""
cursor.execute(query4)
for row in cursor.fetchall():
    print(row)


print("----------------")




# toplists by country
print("toplists by country")
query7 = """

SELECT 

    toplists.name,
    
    countries.name
FROM
    countries
    
    
INNER JOIN
    toplists ON countries.code = toplists.country_code
GROUP BY
    countries.name
ORDER BY
    toplists.name DESC


"""

cursor.execute(query7)
for row in cursor.fetchall():
    print(row)

print("----------------")




# toplists count by country
print("toplists count by country")

query11 = """
SELECT COUNT(DISTINCT toplists.name) AS toplists_count, countries.name
FROM 
    countries
INNER JOIN  
    toplists ON countries.code = toplists.country_code 
GROUP BY


    countries.name
ORDER BY
    toplists_count DESC
    
"""

cursor.execute(query11)
for row in cursor.fetchall():
    print(row)
print("----------------")
print("Best Country to Prioritize: Spain could be a strong choice for your limited marketing budget. It has high visibility in top lists, indicating potential consumer interest and market presence. Although its number of wineries and wines produced are lower compared to France and the USA, its top list performance suggests that marketing efforts could yield substantial returns by tapping into a market with proven consumer engagement.")
print("----------------")
