#Class address
class Address:
    def __init__(self, street: str, number: int, city: str, zip_code: str):
        self.street = street
        self.number = number
        self.city = city
        self.zip_code = zip_code

    def __str__(self) -> str:
        return f"{self.street} {self.number}, {self.zip_code} {self.city}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Address):
            return False
        return self.street == other.street and self.number == other.number and self.city == other.city and self.zip_code == other.zip_code