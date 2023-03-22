from classes.person import Customer
from classes.deliver import Deliver

#Class bill
class Bill:
    def __init__(self, customer: Customer, deliver: Deliver):
        self.customer = customer
        self.deliver = deliver

    def __str__(self) -> str:
        return f"Bill for {self.customer}:\n{self.deliver}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bill):
            return False
        return self.customer == other.customer and self.deliver == other.deliver