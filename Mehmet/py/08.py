# -- Wine Popularity by User Demographics
# -- Question: Which wines are most popular among different user demographics (e.g., by country or region of the users)?
# -- Data Needed: User demographics (potentially inferred from users_count in countries), wine ratings (wines, vintages).




import sqlite3
import pandas as pd

db_path = r'Mehmet/db/vivino.db'

query = '''
SELECT 
    r.name as region_name,
    count(w.id) total_wine,
    AVG(ratings_average) AS rating_averages,
    count(ratings_count) AS rating_count
FROM wines w
JOIN regions r ON w.region_id = r.id
GROUP BY r.name
ORDER BY total_wine DESC
LIMIT 10;
'''

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(query, conn)

conn.close()

csv_file_path = '08.csv'

df.to_csv(csv_file_path, index=False)

print(f"Data has been written to {csv_file_path}")






