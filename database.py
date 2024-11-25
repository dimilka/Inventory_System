import sqlite3

DB_FILE = "inventory.db"

def initialize_db():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            quantity INTEGER NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def add_product(name, quantity):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (name, quantity))
    connection.commit()
    connection.close()

def delete_product(name):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE name = ?", (name,))
    connection.commit()
    connection.close()

def update_product_quantity(name, quantity):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET quantity = ? WHERE name = ?", (quantity, name))
    connection.commit()
    connection.close()

def list_products():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT name, quantity FROM inventory")
    products = [{"name": row[0], "quantity": row[1]} for row in cursor.fetchall()]
    connection.close()
    return products
