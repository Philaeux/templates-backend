import uuid
from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError


def create_jwt_token(key: str, user_id: uuid.UUID):
    """Create a login JWT containing the user id."""
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(UTC) + timedelta(days=60),
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    return token


def check_user(context):
    """Check headers for a login JWT and return the user_id if valid."""
    authorization_header = context["request"].headers.get("Authorization")
    if authorization_header and authorization_header.startswith("Bearer "):
        token = authorization_header.split("Bearer ")[1]

        try:
            payload = jwt.decode(token, context["settings"].jwt_secret_key, algorithms="HS256")
            user_id = payload.get("sub")
            return user_id
        except JWTError:
            return None
    return None
