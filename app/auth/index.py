from fastapi import Header
from app.environment.index import JWT_TOKEN
from app.error_handling.index import UnauthorizedError, ForbiddenError


def verify_token(auth_token: str = Header(default=None)):
    if not auth_token:
        raise UnauthorizedError("Authorization token is missing")
    if auth_token != JWT_TOKEN:
        raise ForbiddenError("Authorization token is invalid")
    return auth_token
