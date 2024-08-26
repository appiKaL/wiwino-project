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
SELECT wines.name, wines.ratings_average, wines.ratings_count
FROM wines
WHERE wines.ratings_count > 20000 AND wines.ratings_average >= 4.6
ORDER BY wines.ratings_average DESC, wines.ratings_count DESC
LIMIT 10;
"""

# Execute the query
cursor.execute(query1)

# Fetch all results from the executed query
rows = cursor.fetchall()

# Extract column names from cursor description
columns = [description[0] for description in cursor.description]

# Write results to a CSV file
with open('1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write column headers to the CSV file
    writer.writerow(columns)
    
    # Write data rows to the CSV file
    writer.writerows(rows)

print("CSV file '1.csv' has been saved successfully.")

# Close the database connection
connexion.close()
