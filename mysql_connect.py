import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Default is often 'root' for XAMPP
            password='',  # XAMPP default has no password
            database='ecommerce'  # Create the database beforehand if needed
        )
        print("Connected to MySQL database successfully")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def execute_queries_from_file(connection, file_path):
    """Execute SQL statements from a file."""
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
        commands = sql_script.split(';')  # Ensure each SQL command ends with ';'
        for command in commands:
            if command.strip():
                execute_query(connection, command)
    except Error as e:
        print(f"Error: '{e}'")
    except FileNotFoundError:
        print("SQL file not found")

def execute_query(connection, query):
    """Execute a single SQL query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error: '{e}'")

# Establish MySQL connection
connection = create_connection()

# Path to the SQL file
sql_file_path = 'SQL.sql'

# Execute SQL file
execute_queries_from_file(connection, sql_file_path)