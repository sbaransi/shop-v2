CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10,2)
);

INSERT INTO products (name, price)
VALUES
('Laptop', 3500.00),
('Mouse', 120.00),
('Keyboard', 250.00);
