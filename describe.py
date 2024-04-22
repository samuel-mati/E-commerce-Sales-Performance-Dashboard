import pandas as pd
from sqlalchemy import create_engine

def import_sales_data(csv_file_path, database_url, table_name='sales'):
    """
    Import specific sales data from a CSV file into the MySQL sales table.
    """
    # Read the necessary columns from the CSV, including Gender
    df = pd.read_csv(csv_file_path, usecols=[
        'Invoice ID', 'Branch', 'customer_id', 'product_id', 
        'Gender', 'Unit price', 'Quantity', 'Date', 
        'Time', 'Payment', 'Rating'
    ])
    
    # Map CSV column names to database column names
    df.rename(columns={
        'Invoice ID': 'invoice_id',
        'Branch': 'branch_id',  # Assuming conversion from branch name to branch_id is handled
        'Gender': 'customer_gender',  # Map Gender from CSV to customer_gender in the database
        'Unit price': 'unit_price',
        'Quantity': 'quantity',
        'Date': 'date',
        'Time': 'time',
        'Payment': 'payment',
        'Rating': 'rating'
    }, inplace=True)

    # Convert date and time to the correct SQL format
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df['time'] = pd.to_datetime(df['time']).dt.strftime('%H:%M:%S')

    # Create SQLAlchemy engine
    engine = create_engine(database_url)
    
    # Insert data into the database
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print("Data imported successfully")

# Database connection settings
user = 'root'
password = ''  # Your MySQL root password
host = 'localhost'
database = 'ecommerce'
database_url = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

# Path to the CSV file
csv_file_path = 'supermarket_sales.csv'  # Ensure this path is correct

# Call the function to import data
import_sales_data(csv_file_path, database_url)
