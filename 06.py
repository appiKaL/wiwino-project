import sqlite3
import pandas as pd

db_path = r"c:\Users\mehme\becode---\BECODE___PROJECTS\02.WIWINO_sql\wiwino\db\vivino.db"

conn = sqlite3.connect(db_path)

query = '''
SELECT *
FROM wines
WHERE name LIKE '%Cabernet Sauvignon%'
ORDER BY ratings_average DESC, ratings_count DESC
LIMIT 5;
'''

df = pd.read_sql_query(query, conn)

conn.close()
csv_file_path = '07.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")