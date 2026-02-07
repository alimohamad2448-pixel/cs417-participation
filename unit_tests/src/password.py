
def validate_password():

    password: str) -> bool:
    
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if len password < 8:
        return False

    has_uppercase = any(c.isupper() for c in password)

    has_digit = any(c.isupper() for c in password)

    return has_uppercase and has_digit