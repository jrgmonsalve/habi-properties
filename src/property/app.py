from http import HTTPStatus
from typing import List

from src.property.application.Controllers.property_controller import PropertyController
from src.property.application.Entities.property_response import PropertyResponse
from src.property.domain.property_repository import PropertyRepository
from src.property.infrastructure.repositories.mysql_property_repository import MysqlPropertyRepository
from src.shared.CustomExceptions import UrlNotFound, MethodNotAllowed
from src.shared.utilities import extrac_params_from_path, api_response_handler


class App:

    @staticmethod
    #@api_response_handler
    def get_response(method: str, path: str):
        return "hola"
#        if "GET" == method:
#            if "/property" == path.split("?")[0]:
''' property_repository: PropertyRepository = MysqlPropertyRepository()
                property_controller: PropertyController = PropertyController(property_repository)
                filters = extrac_params_from_path(path)
                properties_response: List[PropertyResponse] = property_controller.get_by_filters(filters)
                return properties_response, HTTPStatus.OK'''
#            raise UrlNotFound
#        raise MethodNotAllowed
