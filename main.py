import database
from product import Product
from report import generate_report

def main():
    print("Добро пожаловать в Advanced Inventory System!")
    database.initialize_db()

    while True:
        print("\nДоступные команды:")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Обновить количество")
        print("4. Показать список товаров")
        print("5. Экспортировать отчёт")
        print("6. Выйти")

        choice = input("Введите номер команды: ")

        if choice == "1":
            name = input("Введите название товара: ")
            quantity = int(input("Введите количество: "))
            database.add_product(name, quantity)
        elif choice == "2":
            name = input("Введите название товара для удаления: ")
            database.delete_product(name)
        elif choice == "3":
            name = input("Введите название товара: ")
            quantity = int(input("Введите новое количество: "))
            database.update_product_quantity(name, quantity)
        elif choice == "4":
            products = database.list_products()
            for product in products:
                print(f"{product['name']}: {product['quantity']} шт.")
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("Выход...")
            break
        else:
            print("Неверная команда! Попробуйте ещё раз.")

if __name__ == "__main__":
    main()
