# 🚧 Work in progress



# API vs. Interface – Technical Comparison

This mini project demonstrates two integration approaches:

1. File-based batch interface (CSV): Export and import between systems
2. REST API (HTTP/JSON): Real-time data access

Goal: To practically compare architectural and technical differences between integration patterns.



## Libraries Used (Simple Explanation)

**pandas**  
Used for handling data in table format (similar to Excel).  
Reads data from the database and exports it as a CSV file.

**sqlalchemy**  
Database connection layer for Python.  
Creates and manages the connection to PostgreSQL.

**psycopg2-binary**  
PostgreSQL driver used by SQLAlchemy.  
Enables communication between Python and the database.

**pathlib**  
Used for managing file paths.  
Ensures the correct folder structure for file storage.

## Technical Stack



- PostgreSQL (Database)

- Docker (Containerized environment)

- pandas (Data extraction \& export)

- SQLAlchemy (Database connection abstraction layer)

- psycopg2 (PostgreSQL driver)

- pathlib (File system handling)



