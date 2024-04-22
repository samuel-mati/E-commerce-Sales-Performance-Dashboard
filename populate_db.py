import pandas as pd
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine

def create_connection():
    """Create a connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ecommerce'
        )
        print("Connected to MySQL database successfully")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def import_csv_data(csv_file, table_name):
    """Import data from a CSV file into a specified table using the existing connection."""
    df = pd.read_csv(csv_file, usecols=['customer_id', 'Customer type'])  
    # Specify the connection parameters directly in the engine creation
    df.columns = ['customer_id','customer_type']

    # Drop duplicates to ensure each product ID is unique
    df = df.drop_duplicates(subset='customer_id', keep='first')
    user = 'root'
    password = ''  # Use your actual password here if set
    host = 'localhost'
    database = 'ecommerce'
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print("Data imported successfully")

# Establish MySQL connection
connection = create_connection()



# Use raw string for the path to avoid escape sequence errors
csv_file_path = 'supermarket_sales.csv'
import_csv_data(csv_file_path, 'customers')
