import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# DB connection
url = "postgresql+psycopg://demo:demo@localhost:5433/integration_demo"
engine = create_engine(url)

# Path to exported CSV file
csv_path = Path("data/outbound/customers_export.csv")

# Read CSV file
df = pd.read_csv(csv_path)

# Import data into a new table
df.to_sql(
    "customers_import",
    engine,
    if_exists="replace",
    index=False
)

print("Import done!")