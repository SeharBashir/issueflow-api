from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, resource: str, resource_id: int):
        super().__init__(
            status_code=404,
            detail=f"{resource} with id {resource_id} not found"
        )


class ConflictException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=409,
            detail=detail
        )


class BadRequestException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=400,
            detail=detail
        )