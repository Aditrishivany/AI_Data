from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed):
    return check_password_hash(hashed, password)

def response(status, message, data=None):
    return {
        "status": status,
        "message": message,
        "data": data
    }