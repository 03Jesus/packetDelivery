class PayMethod:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PayMethod):
            return False
        return self.name == other.name and self.description == other.description