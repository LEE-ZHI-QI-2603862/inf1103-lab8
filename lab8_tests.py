from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())

supplier = Supplier("S001", "Tech Supplies", "sales@tech.com")

physical_product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)

digital_product = DigitalProduct("P002", "Software", 99.90, 45, 1500, supplier)

print("--- PHYSICAL PRODUCT DETAILS ---")
show_product_details(physical_product)

print()

print("--- DIGITAL PRODUCT DETAILS ---")
show_product_details(digital_product)

print("\n--- INVENTORY LSP TEST ---")

inventory = Inventory()

inventory.add_product(physical_product)
inventory.add_product(digital_product)

inventory.display_all()