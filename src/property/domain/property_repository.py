from abc import ABC, abstractmethod
from typing import Dict, Optional

from src.property.domain.property import Property


class PropertyRepository(ABC):

    @abstractmethod
    def find_with_query_filters(self, filters: Dict) -> Optional[Property]:
        raise NotImplementedError
