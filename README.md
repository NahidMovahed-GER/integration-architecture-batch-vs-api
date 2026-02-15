# 🚧 Work in progress



# API vs. Interface – Technical Comparison

This mini project demonstrates two integration approaches:

1. File-based batch interface (CSV): Export and import between systems
2. REST API (HTTP/JSON): Real-time data access

Goal: To practically compare architectural and technical differences between integration patterns.



## Libraries Used



- **pandas**  

&nbsp; Used for data handling and transformation.  

&nbsp; Reads SQL query results into a DataFrame and exports data to CSV.



- **sqlalchemy**  

&nbsp; Provides the database connection layer.  

&nbsp; Acts as a bridge between Python and PostgreSQL.



- **psycopg2-binary**  

&nbsp; PostgreSQL driver required by SQLAlchemy to communicate with the database.



- **pathlib**  

&nbsp; Handles file paths in a clean and platform-independent way.





## Technical Stack



- PostgreSQL (Database)

- Docker (Containerized environment)

- pandas (Data extraction \& export)

- SQLAlchemy (Database connection abstraction layer)

- psycopg2 (PostgreSQL driver)

- pathlib (File system handling)



