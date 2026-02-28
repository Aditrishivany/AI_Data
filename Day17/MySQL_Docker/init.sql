CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INT
);

INSERT INTO employees (name, department, salary)
VALUES 
('Aditi', 'HR', 40000),
('Rahul', 'IT', 60000),
('Sneha', 'Finance', 50000);
