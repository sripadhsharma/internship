import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection parameters
hostname = 'localhost'
database = 'postgres'  # Replace with the actual database name
username = 'postgres'
pwd = 'Tippa123'
port_id = 5432
# Read the Excel file into a pandas DataFrame
excel_file_path = r'C:\Users\Thipparaju Sripadh\Downloads\MOCK_DATA.xlsx'
df = pd.read_excel(excel_file_path)
# Display the DataFrame (optional)
print(df)
# Create a SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}')
# Drop the index column before writing to the PostgreSQL database
# Write the DataFrame to the PostgreSQL database
table_name = 'employee'  # Replace with your desired table name
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False,schema='staff',chunksize=95)