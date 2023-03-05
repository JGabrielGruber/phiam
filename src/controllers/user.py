from hug import types
from falcon import HTTP_201, HTTP_204, HTTP_404
from uuid import uuid4

from repositories import user as user_repository
from utils.email_type import email as email_type

def get_users() -> list:
    return user_repository.get_users()

def add_user(
    name: types.text, email: email_type,
    response, **kwargs,
) -> dict:
    user = {**kwargs}
    uuid = uuid4().hex
    user['uuid'] = uuid
    user['name'] = name
    user['email'] = email
    user = user_repository.add_user(user, uuid)
    if user is not None:
        response.status = HTTP_201
    return user

def get_user(uuid: types.uuid, response) -> dict:
    user = user_repository.get_user(uuid.hex)
    if user is not None:
        return user
    response.status = HTTP_404
    return { 'error': 'User not found' }

def update_user(
    uuid: types.uuid, name: types.text,
    email: email_type, response, **kwargs,
) -> dict:
    user = {**kwargs}
    uuid = uuid.hex
    user['uuid'] = uuid
    user['name'] = name
    user['email'] = email
    return user_repository.update_user(user, uuid)

def delete_user(uuid: types.uuid, response) -> None:
    user_repository.delete_user(uuid.hex)
    response.status = HTTP_204
