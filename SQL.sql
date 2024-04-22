
-- Create table 'branches' with branch_id as primary key and city as a varchar
CREATE TABLE branches (
  branch_id CHAR(1) PRIMARY KEY,
  city VARCHAR(255)
);


-- Create table 'customers' with customer_id as primary key and customer_type as an enum
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_type ENUM('Member', 'Normal')
);


-- Create table 'products' with product_id as primary key and product_line as a varchar
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_line VARCHAR(255)
);


-- Create table 'sales' with invoice_id as primary key and various sales-related fields
CREATE TABLE sales (
  invoice_id VARCHAR(255) PRIMARY KEY,
  branch_id CHAR(1),
  customer_id INT,
  product_id INT,
  unit_price DECIMAL(10,2),
  quantity INT,
  total DECIMAL(10,2),
  date DATE,
  time TIME,
  payment ENUM('Cash', 'Credit card', 'Ewallet'),
  rating DECIMAL(3,1),
  customer_gender ENUM('Male', 'Female')
);


-- Add foreign key constraint for branch_id referencing branches table
ALTER TABLE sales ADD CONSTRAINT fk_branch_id FOREIGN KEY (branch_id) REFERENCES branches(branch_id);


-- Add foreign key constraint for customer_id referencing customers table
ALTER TABLE sales ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);


-- Add foreign key constraint for product_id referencing products table
ALTER TABLE sales ADD CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products(product_id);