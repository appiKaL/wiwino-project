import sqlite3
import pandas as pd

db_path = r'C:\Users\mehme\becode---\BECODE___PROJECTS\02.WIWINO_sql\wiwino-project\db\vivino.db'

query = '''
SELECT
    w.name as wine_name,
	ratings_count,
	v.price_euros as rating_per_price,	
	ratings_average as rating
FROM 
    vintages 
join wines w v on v.wine_id = w.id
JOIN 
    regions r ON r.id = w.region_id
JOIN 
    countries c ON r.country_code = c.code
ORDER BY rating DESC
LIMIT 10;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '01.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")