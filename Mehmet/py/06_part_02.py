import sqlite3
import pandas as pd

db_path = r'C:\Users\mehme\becode---\BECODE___PROJECTS\02.WIWINO_sql\wiwino-project\Mehmet\db\vivino.db'

conn = sqlite3.connect(db_path)

query = '''
SELECT
    r.country_code AS country_code,
    c.name AS country_name,

    AVG(v.ratings_average) AS average_rating
FROM
    vintages v
JOIN wines w ON v.wine_id = w.id 
JOIN regions r ON w.region_id = r.id
join countries c ON r.country_code = c.code
GROUP BY
    r.country_code, c.name
ORDER BY
    average_rating DESC;
'''

df = pd.read_sql_query(query, conn)

conn.close()
csv_file_path = '06_part_02.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")