# E-Commerce Data Analysis  

## Overview  
This project analyzes e-commerce data using **PostgreSQL** and **SQL** queries.  
The goal is to explore customer behavior, product categories, and order details through relational database queries.  

## Tech Stack  
- **PostgreSQL** – relational database  
- **SQL** – data analysis queries  

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

## Screenshots 
<img width="1381" height="909" alt="Снимок экрана 2025-09-21 175041" src="https://github.com/user-attachments/assets/4a7bf2fb-e88c-4ce6-96ee-9dfca08bfb2d" />
<img width="811" height="929" alt="Снимок экрана 2025-09-21 180702" src="https://github.com/user-attachments/assets/16f9458f-0fee-4790-a3eb-59928b590ac1" />
<img width="1111" height="633" alt="Снимок экрана 2025-09-21 180648" src="https://github.com/user-attachments/assets/f163ab2d-40fa-4fab-a315-e784902ab96d" />
<img width="1381" height="924" alt="Снимок экрана 2025-09-21 180635" src="https://github.com/user-attachments/assets/ff6ae5f6-50be-4df1-8d8a-7a04a9379a94" />
<img width="1386" height="903" alt="Снимок экрана 2025-09-21 180622" src="https://github.com/user-attachments/assets/ca1b1ec2-82b1-4390-bc87-c02e1666600a" />
<img width="823" height="917" alt="image" src="https://github.com/user-attachments/assets/b7d96cf7-c9ef-4f24-9a53-2af6ec300dad" />
<img width="595" height="391" alt="image" src="https://github.com/user-attachments/assets/2d22cc64-4733-4cdf-80aa-1363ba4a5233" />

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



