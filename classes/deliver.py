from typing import List
from classes.person import Person, Customer, Receiver
from classes.address import Address
from classes.products import Product
#Class deliver
class Deliver:
    def __init__(self, id: int, date: str,
                sender: Customer, receive: Receiver, sender_address: Address,
                receiver_address: Address, contact: Person, products: List[Product]):
        self.id = id
        self.date = date
        self.sender = sender
        self.receive = receive
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.contact = contact
        self.products = products

    def calculate(self) -> float:
        return sum([product.calculate() for product in self.products])

    def __str__(self) -> str:
        products_str = "\n".join([str(product) for product in self.products])
        return f"Delivery ID: {self.id}\n" \
               f"Date: {self.date}\n" \
               f"Sender:\n{self.sender}\n" \
               f"Receiver:\n{self.receive}\n" \
               f"Sender Address:\n{self.sender_address}\n" \
               f"Receiver Address:\n{self.receiver_address}\n" \
               f"Contact:\n{self.contact}\n" \
               f"Products:\n{products_str}\n" \
               f"Total: {self.calculate()} €"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Deliver):
            return False
        return self.products == other.products