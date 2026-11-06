from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product : Product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

    def display_information(self) -> None:
        self.product.display_information()
        print(
            f"{self.product.get_name()} "
            f"x {self.quantity} " 
            f" = ${self.calculate_subtotal():.2f}"
        )