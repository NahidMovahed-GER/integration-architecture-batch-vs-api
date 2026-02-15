CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (name, email)
VALUES
('Max Mustermann', 'max@example.com'),
('Anna Schmidt', 'anna@example.com'),
('John Miller', 'john@example.com');
