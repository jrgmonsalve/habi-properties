from typing import Dict, Optional

from src.property.domain.property import Property
from src.property.domain.property_repository import PropertyRepository


class MysqlPropertyRepository(PropertyRepository):
    def find_with_query_filters(self, filters: Dict) -> Optional[Property]:
        pass