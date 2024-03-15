import pandas as pd
from sqlalchemy import create_engine
# Create Oracle engine
oracle_connection_string = create_engine('oracle://system:Tippa123@localhost:1521/xe')
# Create PostgreSQL engine
postgres_connection_string = create_engine('postgresql://postgres:Tippa123@localhost:5432/postgres')
table_name='sripadh_0'
# Fetch existing data from PostgreSQL
existing_df = pd.read_sql(f"SELECT * FROM {table_name}", postgres_connection_string)
# Fetch data from Oracle
query = f"SELECT * FROM {table_name}"
new_df = pd.read_sql(query, oracle_connection_string)
# Filter out rows that already exist in PostgreSQL
new_rows = new_df[~new_df.isin(existing_df)].dropna()
# Print the number of rows fetched from Oracle
print("Number of rows fetched from Oracle:", len(new_df))
# Print the number of rows to be inserted into PostgreSQL
print("Number of new rows to be inserted into PostgreSQL:", len(new_rows))
# Append new rows to the existing data in PostgreSQL
new_rows.to_sql(name=table_name, con=postgres_connection_string, if_exists="append", index=False)
print("New rows added from Oracle table", table_name, "to PostgreSQL.")