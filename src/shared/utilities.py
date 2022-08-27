import json
from typing import List
from http import HTTPStatus

from src.property.application.Entities.api_response import ApiResponse
from src.shared.CustomExceptions import UrlNotFound, MethodNotAllowed


def api_response_handler(func):
    def wrapper_do_twice(*args, **kwargs):
        body = {
            "status": "FAIL",
            "data": "",
            "error": "Unknown, check logs."
        }
        api_response: ApiResponse = ApiResponse(status=HTTPStatus.INTERNAL_SERVER_ERROR, body=body)

        try:
            result_controller, status_code = func(*args, **kwargs)
            body["status"] = "SUCCESS"
            body["data"] = [item.__dict__ for item in result_controller]
            body["error"] = ""
            api_response.status = status_code
            api_response.body = body

        except UrlNotFound as ex:
            body["error"] = ex.message
            api_response.status = ex.STATUS_CODE
        except MethodNotAllowed as ex:
            body["error"] = ex.message
            api_response.status = ex.STATUS_CODE
        except Exception as e:
            print(e)

        return json.dumps(api_response.__dict__)

    return wrapper_do_twice


def extrac_params_from_path(path: str) -> List:
    final_params = []

    try:
        params = path.split("?")[1]

        for param in params.split("&"):
            split_param = param.split("=")
            final_params.append({
                "key": split_param[0],
                "value": split_param[1]
            })

    except IndexError:
        print("Error get values: the path doesn't have right structure ej: /asd?asd=123")

    return final_params
