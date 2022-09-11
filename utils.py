from re import match

def validate_register(username, password):
    # A valid username is at least 5 characters long
    if len(username) < 5:
        return False
    
    # A valid password is at least 8 characters long,
    # Has at least one uppercase and lower case letter
    # Has at least one number and special character

    password_expr = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$'

    return match(password_expr, password)
    
