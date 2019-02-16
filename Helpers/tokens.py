import jwt
import datetime
from Helpers.utils import assert_found, assert_valid
from functools import wraps
from BloodDonation.settings import SECRET_KEY
from Helpers.serializers import get_model_json

def token_required(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION", None)
        assert_found(token, "Access token not found")
        return func(request, *args, **kwargs)
    return decorator


def generate_token(user):
    data = { 'user': get_model_json(user) }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')

def get_token_data(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.InvalidTokenError as e:
        print(e)
        return None
    return payload


def get_user(token):
    user = get_or_none(User, username=get_token_data(token)['user']['username'])
    assert_found(user, "No user found")
    return user

