import sqlite3
import csv


connexion = sqlite3.connect('vivino.db')
cursor = connexion.cursor()



# SQL sorgusu
query = """
SELECT DISTINCT wines.name AS wines_name,keywords.name AS keywords_name,keywords_wine.group_name
FROM wines
INNER JOIN keywords_wine ON wines.id = keywords_wine.wine_id
INNER JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE ( keywords.name LIKE '%coffee%' OR keywords.name LIKE '%toast%' OR keywords.name LIKE '%green apple%' OR keywords.name LIKE '%cream%' OR keywords.name LIKE '%citrus%' )AND keywords_wine.count >= 10 AND ( wines_name IS NOT NULL OR keywords_name IS NOT NULL OR group_name IS NOT NULL )
ORDER BY wines.name, keywords.name, keywords_wine.group_name;

"""

# Sorguyu çalıştırma
cursor.execute(query)
rows = cursor.fetchall()

# Sütun isimlerini alma
columns = [description[0] for description in cursor.description]

# Verileri CSV dosyasına yazma
with open('4.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(columns)  # Başlık satırını yazma
    writer.writerows(rows)  # Verileri yazma

print("CSV dosyası '4.csv' olarak kaydedildi.")

# Bağlantıyı kapatma
connexion.close()
