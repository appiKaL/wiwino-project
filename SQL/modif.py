import sqlite3
import pandas as pd



# conn = sqlite3.connect('C:\Users\ankin\OneDrive\Desktop\wiwino-project\db\vivino (1).db')
conn = sqlite3.connect('C:\\Users\\ankin\\OneDrive\\Desktop\\wiwino-project\\db\\vivino (1).db')


create_table_sql = '''
CREATE TEMPORARY TABLE wine_performance AS
SELECT 
    w.name as wine_name,
    ROUND(SUM(v.ratings_average * v.ratings_count) / SUM(v.ratings_count), 2) AS ratings_average,
    SUM(v.ratings_count) AS ratings_count,
    ROUND(SUM(v.ratings_average * v.ratings_count) / SUM(v.price_euros), 2) AS rating_per_price,
    SUM(v.price_euros) AS price_euros
FROM 
    wines w
JOIN
    vintages v ON w.id = v.wine_id   
WHERE
    v.ratings_count > 0 AND v.price_euros > 0
GROUP BY
    w.name
ORDER BY
    ratings_average DESC, ratings_count DESC, rating_per_price DESC
LIMIT 50;  
'''

# Execute SQL commands
with conn:
    conn.execute(create_table_sql)

# Fetch the results into a DataFrame
df = pd.read_sql_query('SELECT * FROM wine_performance', conn)
conn.close()

# Save the DataFrame to a CSV file
csv_file_path = "01.1.csv"
df.to_csv(csv_file_path, index=False)

print("Data has been successfully exported to .csv")
