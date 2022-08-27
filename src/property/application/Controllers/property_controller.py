from typing import List

from src.property.application.Entities.property_response import PropertyResponse
from src.property.domain.property_repository import PropertyRepository


class PropertyController:
    def __init__(self, repository: PropertyRepository):
        self.repository = repository

    def get_by_filters(self, filters: List) -> List[PropertyResponse]:
        return [
            PropertyResponse(
                address="calle 23 #45-67",
                city="bogota",
                status="comprando",
                price=120000000,
                description="Hermoso apartamento en el centro de la ciudad"
            ),
            PropertyResponse(
                address="carrera 100 #15-90",
                city="bogota",
                status="en_venta",
                price=350000000,
                description="Amplio apartamento en conjunto cerrado"
            )
        ]
