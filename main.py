from database import connect_db, create_table, add_product, update_product_quantity, delete_product, get_product, get_all_products

def menu():
    """Отображает меню для управления инвентарем."""
    print("Добро пожаловать в Inventory Management System")
    print("1. Добавить товар")
    print("2. Обновить количество товара")
    print("3. Удалить товар")
    print("4. Показать все товары")
    print("5. Найти товар по имени")
    print("6. Выйти")

def main():
    create_table()  # Убедимся, что таблица существует
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название товара: ")
            quantity = int(input("Введите количество: "))
            try:
                add_product(cursor, name, quantity)
                conn.commit()
                print("Товар добавлен успешно!")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            name = input("Введите название товара: ")
            quantity = int(input("Введите новое количество: "))
            update_product_quantity(cursor, name, quantity)
            conn.commit()
            print("Количество обновлено успешно!")

        elif choice == "3":
            name = input("Введите название товара для удаления: ")
            delete_product(cursor, name)
            conn.commit()
            print("Товар удален успешно!")

        elif choice == "4":
            products = get_all_products(cursor)
            for product in products:
                print(f"Товар: {product['name']}, Количество: {product['quantity']}")

        elif choice == "5":
            name = input("Введите название товара для поиска: ")
            product = get_product(cursor, name)
            if product:
                print(f"Товар найден: {product['name']}, Количество: {product['quantity']}")
            else:
                print("Товар не найден.")

        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

    conn.close()

if __name__ == "__main__":
    main()
