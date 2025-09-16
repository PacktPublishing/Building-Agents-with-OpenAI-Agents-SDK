import sqlite3

# Set up SQLite DB
conn = sqlite3.connect("paper_data.db")
cursor = conn.cursor()

# Delete orders table if it exists
cursor.execute("DROP TABLE IF EXISTS orders")
# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    authorization_key TEXT,
    order_status TEXT
)
""")
# Insert fake order data
orders_data = [
    (1001, "154857", "shipped"),
    (1002, "154857", "processing"),
    (1003, "958542", "delivered"),
    (1004, "445720", "cancelled"),
]
cursor.executemany("INSERT OR IGNORE INTO orders (order_id, authorization_key, order_status) VALUES (?, ?, ?)", orders_data)
conn.commit()
conn.close()

def test_query_order_status():
    conn = sqlite3.connect("paper_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT order_status FROM orders WHERE order_id = 1003;")
    result = cursor.fetchone()
    conn.close()
    print("Test Query Result:", result)

def test_query_user():
    conn = sqlite3.connect("paper_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, email FROM users WHERE user_id = 2;")
    result = cursor.fetchone()
    conn.close()
    print("Test User Query Result:", result)

if __name__ == "__main__":
    test_query_order_status()
    test_query_user()
