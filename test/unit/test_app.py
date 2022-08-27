import json

from src.property.app import App
from src.property.application.Entities.api_response import ApiResponse


def test_get_response_one_filter_ok():
    # Arrange
    method = "GET"
    path = "/property?year=2000"

    properties = [{'address': 'calle 23 #45-67', 'city': 'bogota', 'status': 'comprando', 'price': 120000000,
                   'description': 'Hermoso apartamento en el centro de la ciudad'},
                  {'address': 'carrera 100 #15-90', 'city': 'bogota', 'status': 'en_venta', 'price': 350000000,
                   'description': 'Amplio apartamento en conjunto cerrado'}]

    body = {
        "status": "SUCCESS",
        "data": properties,
        "error": ""
    }
    expected: ApiResponse = ApiResponse(status=200, body=body)

    # Act
    response = App.get_response(method, path)

    # Assert
    print("response")
    print(response)
    print("json.dumps(expected.__dict__)")
    print(json.dumps(expected.__dict__))
    assert response == json.dumps(expected.__dict__)
