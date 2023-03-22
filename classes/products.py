class Product:
    W_GR_100 = 1.0
    def __init__(self, id: int, weight: float, description: str, cost: float):
        self.id = id
        self.weight = weight
        self.description = description
        self.cost = cost

    def calculate(self) -> float:
        return self.weight * self.W_GR_100 * self.cost

    def __str__(self) -> str:
        return f"Product {self.id}: {self.description} ({self.weight} g) - {self.cost} €"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id
    
#Standard Package derived from Product
class StandardPackage(Product):
    def __init__(self, id: int, weight: float, description: str, cost: float, quantity: int):
        super().__init__(id, weight, description, cost)
        self.quantity = quantity

    def calculate(self) -> float:
        return self.quantity * super().calculate()

    def __str__(self) -> str:
        return f"Standard Package {self.id}: {self.description} ({self.weight} g) - {self.cost} € ({self.quantity} pcs)"

#Overweight Package derived from Product
class OverweightPackage(Product):
    def __init__(self, id: int, weight: float, description: str, cost: float, weight_limit: float):
        super().__init__(id, weight, description, cost)
        self.weight_limit = weight_limit

    def calculate(self) -> float:
        if self.weight > self.weight_limit:
            return self.weight_limit * super().calculate() + (self.weight - self.weight_limit) * super().calculate() * 2
        else:
            return super().calculate()

    def __str__(self) -> str:
        return f"Overweight Package {self.id}: {self.description} ({self.weight} g) - {self.cost} € ({self.weight_limit} g limit)"