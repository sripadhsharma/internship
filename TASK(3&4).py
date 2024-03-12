import pandas as pd
from sqlalchemy import create_engine, types
# Excel file path
excel_file_path = 'C:\\Users\\Thipparaju Sripadh\\Downloads\\newfile.xlsx'
# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
# Display the DataFrame (optional)
print(df)
# Create a SQLAlchemy engine for Oracle
oracle_connection_string = create_engine(f'oracle+cx_oracle://system:Tippa123@localhost:1521/xe')
# Define Oracle-specific column data types
column_data_types = {'Emp_name': types.VARCHAR(50), 'Emp_id': types.NUMERIC, 'Emp_dept': types.VARCHAR(50), 'Emp_joining_date': types.TIMESTAMP, 'Last_updated': types.TIMESTAMP}
# Create the table with specified data types
df.to_sql(name='sripadh_0', con=oracle_connection_string, if_exists='replace', index=False, dtype=column_data_types)
