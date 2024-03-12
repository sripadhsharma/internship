import pandas as pd
from sqlalchemy import create_engine
# Table name (assuming 'info' exists in Oracle)
# Create Oracle engine
oracle_connection_string = create_engine('oracle://system:Tippa123@localhost:1521/xe')
# Create PostgreSQL engine
postgres_connection_string = create_engine('postgresql://postgres:Tippa123@localhost:5432/postgres')
# Fetch data from Oracle
query = f"SELECT * FROM {'sripadh_0'}"
df = pd.read_sql(query, oracle_connection_string)
# Insert data into PostgreSQL
df.to_sql(name='sripadh_0', con=postgres_connection_string, if_exists="replace", index=False)
print(f"Data from Oracle table '{'sripadh_0'}' loaded into PostgreSQL.")