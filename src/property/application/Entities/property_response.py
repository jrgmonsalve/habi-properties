class PropertyResponse:
    def __init__(
            self,
            address: str,
            city: str,
            status: str,
            price: int,
            description: str
    ):
        self.address: str = address
        self.city: str = city
        self.status: str = status
        self.price: int = price
        self.description: str = description
