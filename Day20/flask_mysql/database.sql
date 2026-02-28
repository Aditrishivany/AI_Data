CREATE DATABASE flaskdb;
USE flaskdb;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
);

INSERT INTO students (name, age, course) VALUES
('Divya', 21, 'Python'),
('Anita', 22, 'Java'),
('Kiran', 20, 'Full Stack');
	
    CREATE TABLE  todo (
     id INT PRIMARY KEY AUTO_INCREMENT,
     title VARCHAR(200),
     status VARCHAR(20)
 );	
 create table contacts(
id INT PRIMARY KEY AUTO_INCREMENT,
name varchar(100),
phone varchar(100),
email varchar(100)
);
 create table products(
id int primary key auto_increment,
name varchar(100),
 price DECIMAL(10,2),
    description TEXT
    );
    INSERT INTO products (name, price, description) VALUES
('Laptop', 500.00, '15-inch laptop'),
('Mouse', 20.00, 'Wireless mouse'),
('Keyboard', 35.00, 'Mechanical keyboard');


CREATE TABLE  blogs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    content TEXT
);
INSERT INTO blogs (title, content) VALUES
('My First Blog', 'This is the content of my first blog.'),
('Flask Tips', 'Tips and tricks for Flask development.'),
('Python Basics', 'Introduction to Python programming.');

CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO employees (name, department, email) VALUES
('Alice', 'HR', 'alice@example.com'),
('Bob', 'IT', 'bob@example.com'),
('Charlie', 'Sales', 'charlie@example.com'),
('David', 'IT', 'david@example.com');

CREATE TABLE IF NOT EXISTS quotes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    author VARCHAR(100),
    quote TEXT
);

INSERT INTO quotes (author, quote) VALUES
('Albert Einstein', 'Life is like riding a bicycle. To keep your balance, you must keep moving.'),
('Mahatma Gandhi', 'Be the change that you wish to see in the world.'),
('Steve Jobs', 'Stay hungry, stay foolish.');

CREATE TABLE  notes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    content TEXT
);
CREATE TABLE  movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    director VARCHAR(100),
    year INT
);

CREATE TABLE  inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    quantity INT
);

CREATE TABLE  users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100)
);
CREATE TABLE  posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    content TEXT
);

CREATE TABLE comments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT,
    author VARCHAR(50),
    comment TEXT,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

INSERT INTO posts (title, content) VALUES
('First Post', 'Content of the first post.'),
('Second Post', 'Content of the second post.');

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);


INSERT INTO categories (name) VALUES
('Electronics'),
('Clothing'),
('Books');

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100)
);

CREATE TABLE  enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);


INSERT INTO courses (course_name) VALUES ('Python'), ('Flask');

CREATE TABLE  events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200),
    event_date DATE,
    category VARCHAR(100)
);
CREATE TABLE  urls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    long_url TEXT,
    short_code VARCHAR(20) UNIQUE
);