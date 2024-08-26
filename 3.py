import csv

import sqlite3 

connexion=sqlite3.connect('vivino.db')

cursor=connexion.cursor()


query5="""
SELECT DISTINCT wines.winery_id, wines.ratings_count, wines.name  AS wineries_name, wines.ratings_average FROM wines
INNER JOIN wineries ON wineries.name = wines.name
INNER JOIN vintages ON wines.id = vintages.wine_id
WHERE wines.ratings_average > 4.6 AND wines.ratings_count > 41000
ORDER BY wines.ratings_average DESC, wines.ratings_count DESC
LIMIT 3;


"""

cursor.execute(query5)


rows = cursor.fetchall()


columns = [description[0] for description in cursor.description]


with open('3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(columns)
    
    writer.writerows(rows)

print("CSV dosyası '3.csv' olarak kaydedildi.")


connexion.close()
