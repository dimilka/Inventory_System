import sqlite3

def connect_db():
    """Устанавливает соединение с базой данных."""
    conn = sqlite3.connect("inventory.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Создаёт таблицу products, если она не существует."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_product(cursor, name, quantity):
    """Добавляет новый продукт в базу данных."""
    cursor.execute("SELECT COUNT(*) FROM products WHERE name = ?", (name,))
    if cursor.fetchone()[0] > 0:
        raise ValueError(f"Продукт с именем '{name}' уже существует.")
    cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))

def delete_product(cursor, name):
    """Удаляет продукт из базы данных."""
    cursor.execute("DELETE FROM products WHERE name = ?", (name,))

def get_product(cursor, name):
    """Возвращает информацию о продукте."""
    cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
    return cursor.fetchone()

def get_all_products(cursor):
    """Возвращает список всех продуктов."""
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()
