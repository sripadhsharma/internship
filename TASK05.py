import pandas as pd
from sqlalchemy import create_engine
# Create Oracle engine
oracle_connection_string = create_engine('oracle://system:Tippa123@localhost:1521/xe')
# Create PostgreSQL engine
postgres_connection_string = create_engine('postgresql://postgres:Tippa123@localhost:5432/postgres')
table_name='sripadh_0'
# Fetch data from Oracle
query = f"SELECT * FROM {table_name}"
df = pd.read_sql(query, oracle_connection_string)
# Insert data into PostgreSQL
df.to_sql(name='sripadh_0', con=postgres_connection_string, if_exists="replace", index=False)
print("Data from Oracle table 'table_name' loaded into PostgreSQL.")