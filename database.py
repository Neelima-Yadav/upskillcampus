import sqlite3

DATABASE_NAME = "food_delivery.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Customer Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    # Restaurant Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)

    # Menu Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            item_name TEXT,
            price REAL,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
        )
    """)

    # Orders Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            item_name TEXT,
            quantity INTEGER,
            total REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")