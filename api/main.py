from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Database connection
url = "postgresql+psycopg://demo:demo@localhost:5433/integration_demo"
engine = create_engine(url)


@app.get("/customers")
def get_customers():
    query = text("SELECT id, name, email, created_at FROM customers")

    with engine.connect() as connection:
        result = connection.execute(query)

        customers = []

        for row in result:
            customers.append({
                "id": row.id,
                "name": row.name,
                "email": row.email,
                "created_at": row.created_at
            })

    return customers