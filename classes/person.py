from typing import List
from classes.address import Address
from classes.payMethod import PayMethod
#Class person
class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} ({self.address})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.address == other.address
    
#Class customer derived from Person
class Customer(Person):
    def __init__(self, name: str, address: Address, pay_methods: List[PayMethod]):
        super().__init__(name, address)
        self.pay_methods = pay_methods

    def __str__(self) -> str:
        return f"{super().__str__()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Customer):
            return False
        return self.name == other.name and self.address == other.address and self.pay_methods == other.pay_methods
    
#Class receiver derived from Person
class Receiver(Person):
    def __init__(self, name: str, address: Address):
        super().__init__(name, address)

    def __str__(self) -> str:
        return f"{super().__str__()}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Receiver):
            return False
        return self.name == other.name and self.address == other.address