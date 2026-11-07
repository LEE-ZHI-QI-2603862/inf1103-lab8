import json
import os

from inventory import Inventory
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def load_inventory() -> Inventory:
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as f:
            data = json.load(f)

        for item in data:

            supplier_data = item["supplier"]

            supplier = Supplier(
                 supplier_data["supplier_id"], 
                 supplier_data["name"], 
                 supplier_data["contact_email"]
          )

            if item["type"] == "physical":
                 product = PhysicalProduct(
                      item["id"],
                      item["name"],
                      item["price"],
                      item["stock"],
                      item["weight"],
                      supplier
            )
            elif item["type"] == "digital":
                 product = DigitalProduct(
                      item["id"],
                      item["name"],
                      item["price"],
                      item["stock"],
                      item["download_size"],
                      supplier
                )

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found. Starting with empty inventory.")

    return inventory

def save_inventory(inventory) -> None:
    data = []

    for product in inventory.get_products():
        data.append(product.to_dict())

    with open("inventory.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Inventory saved successfully to inventory.json.")


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()

while True:
     print("------------ MENU ------------")
     print("1. Display All Products")
     print("2. Add Product")
     print("3. Update Stock")
     print("4. Search Product")
     print("5. Save Inventory")
     print("6. Exit")
     print("------------------------------")

     option = input("Enter option: ")

     if option == "1":
          inventory.display_all()
     
     elif option == "2":
          print("Add New Product")
          print("1. Physical Product")
          print("2. Digital Product")

          product_type = input("Select product type: ")
          
          product_id = input("Product ID: ")
          name = input("Product Name: ")
          price = float(input("Price: "))
          stock = int(input("Stock Quantity: "))

          print("\nSupplier Information")

          supplier_id = input("Supplier ID: ")
          supplier_name = input("Supplier Name: ")
          supplier_email = input("Supplier Email:")

          supplier = Supplier(supplier_id, supplier_name, supplier_email)

          if product_type == "1":
               weight = float(input("Weight (kg): "))
               product = PhysicalProduct(
                    product_id,
                    name,
                    price,
                    stock,
                    weight,
                    supplier
               )
               
               inventory.add_product(product)
               print("Physical product added successfully!")

          elif product_type == "2":
               download_size = float(
                      input("Download Size (MB): ")
               )
               
               product = DigitalProduct(
                    product_id,
                    name,
                    price,
                    stock,
                    download_size,
                    supplier
               )
               
               inventory.add_product(product)
               print("Digital product added successfully!")
          else:
               print("Invalid product type.")
     
     elif option == "3":
          print("Update Stock")
          
          product_id = input("Enter Product ID: ")
          
          product = inventory.find_product(product_id)
          
          if product is not None:
               print("Product Found:")
               print("Name:", product.get_name())
               print("Current Stock:", product.get_stock())
               
               new_stock = int(input("New Stock Quantity: "))
               
               product.update_stock(new_stock)
               
               print("Stock updated successfully!")
          
          else:
               print("Product not found.")
     
     elif option == "4":
          print("Search Product")
          
          product_id = input("Enter Product ID: ")
          
          product = inventory.find_product(product_id)
          
          if product is not None:
               print("Product Found")
               print("--------------------------------------------")
               
               product.display_information()
               
               print(
                    "Fulfilment: ",
                    product.get_fulfilment_info()
               )

               print("\nSupplier:")
               product.display_supplier_information()
               
               print("--------------------------------------------")
          
          else:
               print("Product not found.")
     
     elif option == "5":
          print("Saving inventory...")
          save_inventory(inventory)

     elif option == "6":
          print("Saving inventory before exit...")
          save_inventory(inventory)
          
          print("Thank you for using Inventory Management System.")
          print("Program terminated.")
          break

     else:
          print("Invalid option.")

