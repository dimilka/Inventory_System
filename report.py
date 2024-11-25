import csv
import database

def generate_report():
    products = database.list_products()
    with open("inventory_report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Quantity"])
        for product in products:
            writer.writerow([product["name"], product["quantity"]])
    print("Отчёт успешно экспортирован в inventory_report.csv")
