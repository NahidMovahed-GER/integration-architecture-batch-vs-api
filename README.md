# 🚧 Work in progress

# API vs. Interface – Technical Comparison

This project demonstrates two integration approaches:

1. File-based batch interface (CSV): Export and import between systems
2. REST API (HTTP/JSON): Real-time data access

Goal: To practically compare architectural and technical differences between integration patterns.

This project simulates a typical enterprise integration scenario.

## Libraries Used (Simple Explanation)

- **pandas**  
Used for handling data in table format (similar to Excel).  
Reads data from the database and exports it as a CSV file.

- **sqlalchemy**  
Database connection layer for Python.  
Creates and manages the connection to PostgreSQL.

- **psycopg2-binary**  
PostgreSQL driver used by SQLAlchemy.  
Enables communication between Python and the database.

- **pathlib**  
Used for managing file paths.  
Ensures the correct folder structure for file storage.



## How It Works

1. Docker runs the PostgreSQL database in a container.
2. SQLAlchemy establishes the database connection.
3. psycopg2 enables communication with PostgreSQL.
4. pandas retrieves the data and converts it into a structured table.
5. The data is exported as a CSV file (file-based batch interface).





