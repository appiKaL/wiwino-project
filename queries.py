import csv
import sqlite3
import sys
import io

# Ensure proper encoding for standard output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Connect to the SQLite database
connexion = sqlite3.connect('vivino.db')
cursor = connexion.cursor()

print("1. We want to highlight 10 wines to increase our sales. Which wines should we choose and why?")

# Define the SQL query to select wines with high ratings and a significant number of reviews
query1 = """
SELECT 
    keywords.name AS wines_taste,
    ROUND(AVG(wines.ratings_average), 1) AS avg_ratings_average,
    ROUND(AVG(wines.acidity), 2) AS avg_acidity,
    ROUND(AVG(wines.intensity), 2) AS avg_intensity,
    ROUND(AVG(wines.sweetness), 2) AS avg_sweetness,
    ROUND(AVG(wines.tannin), 2) AS avg_tannin

FROM wines
INNER JOIN keywords_wine ON wines.id = keywords_wine.wine_id
INNER JOIN keywords ON keywords.id = keywords_wine.keyword_id
WHERE wines.acidity IS NOT NULL
AND wines.intensity IS NOT NULL
AND wines.sweetness IS NOT NULL
AND wines.tannin IS NOT NULL
AND wines.ratings_average IS NOT NULL
GROUP BY keywords.name
ORDER BY avg_ratings_average DESC;
"""

# Execute the query
cursor.execute(query1)

# Fetch all results from the executed query
rows = cursor.fetchall()

# Extract column names from cursor description
columns = [description[0] for description in cursor.description]

# Write results to a CSV file
with open('8.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write column headers to the CSV file
    writer.writerow(columns)
    
    # Write data rows to the CSV file
    writer.writerows(rows)

print("CSV file '8.csv' has been saved successfully.")

# Close the database connection
connexion.close()
