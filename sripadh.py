import psycopg2
import pandas as pd
from sqlalchemy import create_engine
# PostgreSQL connection parameters
hostname = 'localhost'
database = 'postgres'  # Replace with the actual database name
username = 'postgres'
pwd = 'Tippa123'
port_id = 5432
# Connect to PostgreSQL
conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id
)
# Read the Excel file into a pandas DataFrame with a specified encoding
xlsx_file_path = r'C:\Users\Thipparaju Sripadh\Downloads\MOCK_DATA.xlsx'
df = pd.read_excel(xlsx_file_path)
# Display the DataFrame (optional)
print(df)
# Create a SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}')
# Write the DataFrame to the PostgreSQL database
df.to_sql(name='Wissen', con=engine, if_exists='replace', index=False)
# Close the PostgreSQL connection
conn.close()
