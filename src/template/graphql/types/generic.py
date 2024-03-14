import strawberry


@strawberry.type
class ApiError:
    """Endpoint execution failed.
    
    Attributes:
        message: Details about the error
    """
    message: str

@strawberry.type
class ApiSuccess:
    """Endpoint execution succeeded, but there is nothing to return (like a deletetion)
    
    Attributes:
        message: Optional information
    """
    message: str = ""
