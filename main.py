import psycopg2

try:
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="Project",   # название твоей БД
        user="postgres",      # твой пользователь
        password="0000",  # замени на свой пароль
        host="localhost",     # если локально
        port="5432"           # стандартный порт PostgreSQL
    )
    cur = conn.cursor()
    print("✅ Успешное подключение к PostgreSQL")

    # Список запросов
    queries = [
        # Average delivery time (purchase → customer delivery) by state
        """
        SELECT c.customer_state, 
               AVG(o.order_delivered_customer_date - o.order_purchase_timestamp) AS avg_delivery_time
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        GROUP BY c.customer_state
        ORDER BY avg_delivery_time;
        """,

        # Product categories with the highest average item price
        """
        SELECT p.product_category_name, AVG(oi.price) AS avg_price
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY avg_price DESC
        LIMIT 10;
        """,

        # Top 10 customers by total spending (items + freight)
        """
        SELECT c.customer_unique_id, SUM(oi.price + oi.freight_value) AS total_spent
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_unique_id
        ORDER BY total_spent DESC
        LIMIT 10;
        """
    ]

    # Выполняем запросы по очереди
    for i, q in enumerate(queries, start=1):
        print(f"\n▶ Query {i}:")
        cur.execute(q)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    # Закрываем соединение
    cur.close()
    conn.close()
    print("\n🔒 Соединение закрыто")

except Exception as e:
    print("❌ Ошибка при подключении:", e)
