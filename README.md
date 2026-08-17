# 🚧 Work in Progress

## API vs. Interface – Technical Comparison

This project demonstrates two integration approaches:

* **File-based batch interface (CSV)** – completed ✅
* **REST API (HTTP/JSON)** – next step 🚧

The goal is to practically compare the technical differences between a classic file-based interface and a REST API.

---

## Part 1: File-Based Batch Interface

The first part simulates data transfer between two systems using a CSV file.

### Process

```text
PostgreSQL
    ↓
export_to_csv.py
    ↓
customers_export.csv
    ↓
import_from_csv.py
    ↓
customers_import
```

#### Export (`export_to_csv.py`)
* Connects to PostgreSQL
* Reads customer data with SQL
* Exports the data to a CSV file
* Stores the file in `data/outbound`

#### Import (`import_from_csv.py`)
* Reads the exported CSV file
* Connects to PostgreSQL
* Imports the data into the target table `customers_import`

> This simulates a simple file-based data exchange between two systems.

---

## Technical Stack

* **Python** – application logic
* **PostgreSQL** – database
* **Docker** – runs PostgreSQL in a container
* **pandas** – reads and exports data
* **SQLAlchemy** – database connection
* **psycopg** – PostgreSQL driver
* **pathlib** – file path handling

### Libraries Used

* **pandas**: Reads data from PostgreSQL and handles CSV files.
* **SQLAlchemy**: Creates the connection between Python and the database.
* **psycopg**: Enables communication with PostgreSQL.
* **pathlib**: Handles file and folder paths.

---

## Project Structure

```text
integration-architecture-batch-vs-api/
│
├── batch/
│   ├── export_to_csv.py
│   └── import_from_csv.py
│
├── db/
│   └── init/
│
├── docker-compose.yml
└── README.md
```

---

## Next Step

1. The next part of the project will implement a REST API using HTTP/JSON.
2. After that, both integration approaches will be compared directly:  
   **Batch/CSV vs. REST API**
