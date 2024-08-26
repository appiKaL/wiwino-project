import sqlite3
import pandas as pd

db_path = r"c:\Users\mehme\becode---\BECODE___PROJECTS\02.WIWINO_sql\wiwino\db\vivino.db"

conn = sqlite3.connect(db_path)

query1 = '''
SELECT 
    r.country_code AS country_code, 
    c.name AS country_name, 
    avg(w.ratings_average) as average_rating
FROM wines w
JOIN regions r ON w.region_id = r.id
join countries c ON r.country_code = c.code
GROUP BY 
    r.country_code, c.name
ORDER BY
    average_rating DESC;
'''
query2 = '''
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


df1 = pd.read_sql_query(query1, conn)
df2 = pd.read_sql_query(query2, conn)

conn.close()

combined_df = pd.concat([df1, df2], ignore_index=True)

csv_file_path = '06.csv'

df1.to_csv(csv_file_path, index=False)

print(f"Data from the first query has been written to {csv_file_path}")