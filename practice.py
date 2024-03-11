import pandas as pd
from sqlalchemy import create_engine, types
# Excel file path
excel_file_path = 'C:\\Users\\Thipparaju Sripadh\\Downloads\\newfile.xlsx'
# Oracle connection parameters
hostname, service_name, username, pwd, port_id = 'localhost', 'xe', 'SYSTEM', 'Tippa123', 1521
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
# Display the DataFrame (optional)
print(df)
# Create a SQLAlchemy engine for Oracle
oracle_connection_string = f'oracle+cx_oracle://{username}:{pwd}@{hostname}:{port_id}/{service_name}'
engine = create_engine(oracle_connection_string)
# Convert the table name to lowercase
# Define Oracle-specific column data types
column_data_types = {
    'Emp_name': types.VARCHAR(50),
    'Emp_id': types.NUMERIC,
    'Emp_dept': types.VARCHAR(50),
    # Add more columns and their data types as needed
}
# Create the table with specified data types
df.to_sql(name='sripadh_12', con=engine, if_exists='replace', index=False, dtype=column_data_types)
# Commit the changes and close the connection at the end of the script
engine.connect().close()