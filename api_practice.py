import requests
import mysql.connector
from mysql.connector import Error

#api-key:BC3uLIJHXYUq3eoADfoXTLkoU1tJIoioAU5IyScK

# Fetch data from API
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
posts = response.json()

# Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Soccer2003$$',
        database='api'
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS posts (
            id INT PRIMARY KEY,
            userId INT,
            title VARCHAR(255),
            body TEXT
        )
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        insert_query = """
        INSERT INTO posts (id, userId, title, body)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            userId = VALUES(userId),
            title = VALUES(title),
            body = VALUES(body)
        """

        for post in posts:
            values = (post['id'], post['userId'], post['title'], post['body'])
            cursor.execute(insert_query, values)

        # Commit the transaction
        connection.commit()
        print(f"{cursor.rowcount} rows inserted or updated.")

except Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
