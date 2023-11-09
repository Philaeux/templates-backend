import uuid
from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some possible methods include: base class,
    decorator, metaclass. We will use the metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Possible changes to the value of the `__init__` argument do not affect the returned instance."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def create_jwt_token(key: str, user_id: uuid.UUID):
    """Create a login JWT containing the user id."""
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(UTC) + timedelta(days=60),
    }
    token = jwt.encode(payload, key, algorithm="HS256")
    return token


def check_user(key: str, authorization_header: str):
    """Check headers for a login JWT and return the user_id if valid."""
    if authorization_header and authorization_header.startswith("Bearer "):
        token = authorization_header.split("Bearer ")[1]

        try:
            payload = jwt.decode(token, key, algorithms="HS256")
            user_id = payload.get("sub")
            return user_id
        except JWTError:
            return None
    return None
