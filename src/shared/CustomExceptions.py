from http import HTTPStatus

class UrlNotFound(Exception):
    STATUS_CODE = HTTPStatus.NOT_FOUND

    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)


class MethodNotAllowed(Exception):
    STATUS_CODE = HTTPStatus.METHOD_NOT_ALLOWED

    def __init__(self, message="Method not enable"):
        self.message = message
        super().__init__(self.message)