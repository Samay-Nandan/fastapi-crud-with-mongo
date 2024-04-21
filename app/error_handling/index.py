from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


class HTTPExceptionBase(Exception):
    status_code: int
    default_detail: str = "An error occurred"

    def __init__(self, detail: str = None):
        self.detail = detail or self.default_detail


class UnauthorizedError(HTTPExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Unauthorized access"


class ForbiddenError(HTTPExceptionBase):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "Forbidden operation"


class NotFoundError(HTTPExceptionBase):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Resource not found"


def create_json_response(exception: HTTPExceptionBase):
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.detail},
    )


async def handle_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except HTTPExceptionBase as exc:
        return create_json_response(exc)
    except (RequestValidationError, ValidationError) as exc:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Validation error", "errors": exc.errors()},
        )
    except Exception as exc:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": f"An unexpected error occurred: {str(exc)}"},
        )


def setup_error_handling(app):
    app.middleware("http")(handle_exceptions_middleware)
