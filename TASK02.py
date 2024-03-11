import pandas as pd
from sqlalchemy import create_engine, types
from datetime import datetime
# PostgreSQL connection parameters
hostname,database,username,pwd,port_id = 'localhost','postgres','postgres','Tippa123',5432
# Read the Excel file into a pandas DataFrame
excel_file_path = 'C:\\Users\\Thipparaju Sripadh\\Downloads\\newfile.xlsx'
df = pd.read_excel(excel_file_path)
column_data_types = {'Emp_id': types.BIGINT, 'Emp_joining_date': types.TIMESTAMP, 'Last_updated': types.TIMESTAMP}
# Display the DataFrame (optional)
print(df)
# Create a SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}')
# Write the DataFrame to the PostgreSQL database
df.to_sql(name='employee', con=engine, if_exists='replace', index=False, schema='staff', dtype=column_data_types)