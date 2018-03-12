from flask import request

def security(permission='everyone'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            header_permissions = request.headers.get('permissions', [])
            if permission not in header_permissions:
                raise ValueError(f'Could not find permissions {permission}')
            
            return func(*args, **kwargs)
        return wrapper
    return decorator
