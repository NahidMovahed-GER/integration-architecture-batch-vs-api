import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# DB URL = connection string (user, password, host, port, database)
url = "postgresql://demo:demo@localhost:5432/integration_demo"

# Engine = connection object / driver bridge between Python and PostgreSQL
engine = create_engine(url)

# SQL query: read all customers
query = "SELECT * FROM customers"

# Output path + create folder if missing
path = Path("data/outbound/customers_export.csv")
path.parent.mkdir(parents=True, exist_ok=True)

# Extract data and write CSV (file-based batch interface)
pd.read_sql(query, engine).to_csv(path, index=False)

print("Export done!")
