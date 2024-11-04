import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host='localhost',
            port='5433',  
            user='postgres',
            password='',  
            database='a2'
        )
        print("Connected to PostgreSQL database")
        return connection  # Return the connection object if successful

    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None  # Return None if there's an error

def create  


# Try to establish a connection
connection = create_connection()

if connection:
    connection.close()  # Don't forget to close the connection when done
