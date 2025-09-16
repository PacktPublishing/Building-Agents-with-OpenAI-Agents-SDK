import sqlite3

# Set up SQLite DB
conn = sqlite3.connect("customer_details.db")
cursor = conn.cursor()


# Create users table for customer details
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    location TEXT,
    business_type TEXT,
    phone_number TEXT
)
""")
# Insert fake user data
users_data = [
    (1, "Emily", "Clark", "emily.clark@example.com", "New York", "Retail", "555-1234"),
    (2, "Michael", "Nguyen", "michael.nguyen@example.com", "San Francisco", "E-commerce", "555-5678"),
    (3, "Sophia", "Patel", "sophia.patel@example.com", "Chicago", "Wholesale", "555-8765"),
    (4, "David", "Martinez", "david.martinez@example.com", "Houston", "Manufacturing", "555-4321"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO users (user_id, first_name, last_name, email, location, business_type, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)",
    users_data
)
conn.commit()

conn.close()

def test_query_user():
    conn = sqlite3.connect("customer_details.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name, email, location, business_type, phone_number FROM users WHERE user_id = 2;")
    result = cursor.fetchone()
    conn.close()
    print("Test User Query Result:", result)

if __name__ == "__main__":
    test_query_user()
