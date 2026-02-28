DROP DATABASE IF EXISTS ecommerce_db;
CREATE DATABASE ecommerce_db;
USE ecommerce_db;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT
);
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
        ON DELETE SET NULL
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    order_status VARCHAR(50),
    
    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,
        
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE CASCADE
);
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    amount DECIMAL(10,2),
    payment_status VARCHAR(50),
    
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);
-- 10 USERS
INSERT INTO users (name, email, password, phone, address) VALUES
('John Doe','john1@gmail.com','pass123','9000000001','Hyderabad'),
('Jane Smith','jane2@gmail.com','pass123','9000000002','Delhi'),
('Ravi Kumar','ravi3@gmail.com','pass123','9000000003','Mumbai'),
('Priya Sharma','priya4@gmail.com','pass123','9000000004','Chennai'),
('Arjun Reddy','arjun5@gmail.com','pass123','9000000005','Bangalore'),
('Sneha Patil','sneha6@gmail.com','pass123','9000000006','Pune'),
('Kiran Rao','kiran7@gmail.com','pass123','9000000007','Kolkata'),
('Meera Das','meera8@gmail.com','pass123','9000000008','Ahmedabad'),
('Vikram Singh','vikram9@gmail.com','pass123','9000000009','Jaipur'),
('Anita Verma','anita10@gmail.com','pass123','9000000010','Lucknow');

-- 5 CATEGORIES
INSERT INTO categories (category_name, description) VALUES
('Electronics','Electronic gadgets'),
('Clothing','Apparel items'),
('Books','All kinds of books'),
('Home Appliances','Appliances for home'),
('Sports','Sports equipment');

-- 20 PRODUCTS
INSERT INTO products (product_name, description, price, stock_quantity, category_id) VALUES
('Laptop','Gaming Laptop',75000,20,1),
('Smartphone','Android Phone',25000,30,1),
('Headphones','Wireless Headphones',3000,50,1),
('T-Shirt','Cotton T-Shirt',1200,100,2),
('Jeans','Blue Denim',2000,60,2),
('Jacket','Winter Jacket',3500,40,2),
('Novel','Fiction Book',500,80,3),
('Textbook','Academic Book',1500,70,3),
('Microwave','Kitchen Microwave',8000,25,4),
('Refrigerator','Double Door Fridge',45000,15,4),
('Washing Machine','Automatic Washer',30000,10,4),
('Football','Professional Ball',1500,90,5),
('Cricket Bat','English Willow',7000,35,5),
('Tennis Racket','Carbon Fiber',5000,45,5),
('Tablet','Android Tablet',18000,30,1),
('Camera','DSLR Camera',55000,12,1),
('Shoes','Running Shoes',2500,75,2),
('Blender','Kitchen Blender',4000,22,4),
('Yoga Mat','Exercise Mat',800,110,5),
('Smart Watch','Fitness Watch',9000,28,1);

-- 15 ORDERS
INSERT INTO orders (user_id, total_amount, order_status) VALUES
(1,76000,'Pending'),
(2,25000,'Shipped'),
(3,3000,'Delivered'),
(4,3500,'Pending'),
(5,500,'Delivered'),
(6,8000,'Shipped'),
(7,45000,'Pending'),
(8,1500,'Delivered'),
(9,7000,'Shipped'),
(10,1200,'Pending'),
(1,18000,'Delivered'),
(2,55000,'Shipped'),
(3,2500,'Pending'),
(4,4000,'Delivered'),
(5,9000,'Shipped');

-- 30 ORDER ITEMS
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1,1,1,75000),(1,4,1,1200),
(2,2,1,25000),
(3,3,1,3000),
(4,6,1,3500),
(5,7,1,500),
(6,9,1,8000),
(7,10,1,45000),
(8,8,1,1500),
(9,13,1,7000),
(10,4,1,1200),
(11,15,1,18000),
(12,16,1,55000),
(13,17,1,2500),
(14,18,1,4000),
(15,20,1,9000),
(1,12,1,1500),
(2,14,1,5000),
(3,19,1,800),
(4,5,1,2000),
(5,11,1,30000),
(6,1,1,75000),
(7,3,1,3000),
(8,2,1,25000),
(9,9,1,8000),
(10,6,1,3500),
(11,8,1,1500),
(12,4,1,1200),
(13,5,1,2000),
(14,7,1,500);

-- 15 PAYMENTS
INSERT INTO payments (order_id, payment_method, amount, payment_status) VALUES
(1,'Credit Card',76000,'Completed'),
(2,'UPI',25000,'Completed'),
(3,'Debit Card',3000,'Completed'),
(4,'UPI',3500,'Pending'),
(5,'Credit Card',500,'Completed'),
(6,'Net Banking',8000,'Completed'),
(7,'Credit Card',45000,'Pending'),
(8,'UPI',1500,'Completed'),
(9,'Debit Card',7000,'Completed'),
(10,'UPI',1200,'Pending'),
(11,'Credit Card',18000,'Completed'),
(12,'Net Banking',55000,'Completed'),
(13,'UPI',2500,'Pending'),
(14,'Credit Card',4000,'Completed'),
(15,'Debit Card',9000,'Completed');
 select * from users;
 select * from products where price > 1000;
 select * from products where stock_quantity < 10;
 select * from orders where user_id=1;
 update products set price = 80000 where product_id = 1;
 update products set stock_quantity = 9 where product_id = 1;
 update orders set order_status = 'Delivered' where order_id = 1;