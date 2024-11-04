import requests
import psycopg2
from psycopg2 import OperationalError

# API key: BC3uLIJHXYUq3eoADfoXTLkoU1tJIoioAU5IyScK

# Fetch data from API
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
posts = response.json()

# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        port='5433',
        password='',
        database='api'
    )

    if connection:
        print("Connected to PostgreSQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS movies (
            movies_id SERIAL PRIMARY KEY,
            watchmode_id INT,
            title VARCHAR(255),
            original_title VARCHAR(255),
            plot_overview TEXT,
            type VARCHAR(255),
            runtime_minutes INT,
            year INT,
            end_year INT,
            release_date DATE,
            imdb_id VARCHAR(255),
            tmdb_id INT,
            tmdb_type VARCHAR(255),
        )
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        insert_query = """
        INSERT INTO posts (id, user_id, title, body)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            user_id = EXCLUDED.user_id,
            title = EXCLUDED.title,
            body = EXCLUDED.body
        """

        for post in posts:
            values = (post['id'], post['userId'], post['title'], post['body'])
            cursor.execute(insert_query, values)

        # Commit the transaction
        connection.commit()
        print(f"{cursor.rowcount} rows inserted or updated.")

except OperationalError as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection closed")
