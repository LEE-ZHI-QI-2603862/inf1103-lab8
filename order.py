from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print(f"Order ID: {self.__order_id}")
        print("--------------------------------------------")

        for order_line in self.__order_lines:
            order_line.display_information()
            
        print("--------------------------------------------")
        print(f"Total: ${self.calculate_total():.2f}")