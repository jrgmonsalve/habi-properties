from typing import Dict


class ApiResponse:
    def __init__(self, status: int, body: Dict):
        self.status = status
        self.body = body
