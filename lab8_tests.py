from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

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

print("\n--- POLYMORPHISM TEST ---")

polymorphism_inventory = Inventory()

polymorphism_inventory.add_product(physical_product)
polymorphism_inventory.add_product(digital_product)

for product in polymorphism_inventory.get_products():
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())
    print()

print("\n ======== ASSOCIATION TEST ========")

supplier = Supplier("S001", "Tech Supplies", "sales@tech.com")

physical_product = PhysicalProduct("P001", "Laptop", 1200.0, 15, 2.5, supplier)

digital_product = DigitalProduct("P002", "Software", 99.90, 45, 1500, supplier)

print("--- PHYSICAL PRODUCT SUPPLIER ---")
physical_product.display_supplier_information()

print()

print("--- DIGITAL PRODUCT SUPPLIER ---")
digital_product.display_supplier_information()

print("\n========= AGGREGATION TEST =========")

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(physical_product)

print("Inventory A:")
inventory_a.display_all()

inventory_a.remove_product("P001")

print("\nAfter removing product from Inventory A:")

physical_product.display_information()

inventory_b.add_product(physical_product)

print("\nInventory B:")
inventory_b.display_all()

print("Same Product object:", inventory_b.find_product("P001") is physical_product)

print("\n========= COMPOSITION TEST =========")

order1 = Order("O001")

order1.add_order_line(physical_product, 2)
order1.add_order_line(digital_product, 1)

order1.display_order()

order2 = Order("O002")

order2.add_order_line(physical_product, 1)

line1 = order1.get_order_lines()[0]
line2 = order2.get_order_lines()[0]

print("\nSame OrderLine object:", line1 is line2)

print("Same Product object:", line1.get_product() is line2.get_product())

print("\n========= LSP TEST =========")

show_product_details(physical_product)

print()

show_product_details(digital_product)