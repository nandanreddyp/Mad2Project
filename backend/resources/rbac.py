from flask_jwt_extended import get_jwt_identity
from functools import wraps

from database import User



def access_for(roles:[]):
    '''RBAC decorator'''
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            current_user = User.query.filter_by(email=get_jwt_identity()).first()
            if current_user.role not in roles:
                return {'msg':'Not authorized for this end point'}, 403
            return f(*args, **kwargs)
        return decorator_function
    return decorator