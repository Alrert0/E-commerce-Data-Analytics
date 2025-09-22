# Shoplytics

## Overview  
This project analyzes e-commerce data using **PostgreSQL** and **SQL** queries.  
The goal is to explore customer behavior, product categories, and order details through relational database queries.  

##  Database Structure  
Main tables:  
1. `customers` – customer information  
2. `orders` – order details  
3. `order_items` – products within orders  
4. `products` – product information  
5. `sellers` – seller information  
6. `order_payments` – payment details  

## Relationships  
- `customers.customer_id` ↔ `orders.customer_id`  
- `orders.order_id` ↔ `order_items.order_id`  
- `order_items.product_id` ↔ `products.product_id`  
- `order_items.seller_id` ↔ `sellers.seller_id`  
- `orders.order_id` ↔ `order_payments.order_id`  

## ERD
  <img width="1013" height="906" alt="Снимок экрана 2025-09-21 164755" src="https://github.com/user-attachments/assets/d61e82be-440c-4316-bc36-298ab507e4fa" />


## Tools & Resources  

- **PostgreSQL** – main relational database  
- **pgAdmin / DBeaver** – database management tools (optional)  
- **Python 3.10** – for running SQL queries from scripts  
- **psycopg2** – Python library to connect with PostgreSQL  
- **Git & GitHub** – version control and project hosting  
- **Dataset** – public e-commerce dataset (~100k rows, multiple tables)

##  How to Run the Project

1. **Install PostgreSQL** on your computer.  
2. **Create a database**  
3. **Import the dataset** into the database 
4. **Run the SQL queries** from `queries.sql` to check and analyze the data.  
5. **Run the Python script** `main.py` to connect to the database and execute some queries automatically.  



