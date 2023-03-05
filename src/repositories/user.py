import config
import json
import os

os.makedirs(config.USERS_PATH, exist_ok=True)
__users_index = []

try:
    index_file = open(config.USER_FILE)
    file_content = index_file.read()
    __users_index = json.loads(file_content)
    index_file.close()
except FileNotFoundError:
    user_file = open(config.USER_FILE, 'w')
    user_file.write('[]')
    user_file.close()
    __users_index = []

def get_users() -> list:
    users = []
    for index in __users_index:
        with open(config.USERS_PATH + index) as user_file:
            file_content = user_file.read()
        user = json.loads(file_content)
        users.append(user)
    return users

def add_user(user: dict, uuid: str) -> str:
    with open(config.USERS_PATH + uuid, 'w') as user_file:
        user_file.write(json.dumps(user))
    __users_index.append(uuid)
    with open(config.USER_FILE, 'w') as index_file:
        index_file.write(json.dumps(__users_index))
    return user

def get_user(uuid: str):
    if uuid in __users_index:
        with open(config.USERS_PATH + uuid) as user_file:
            file_content = user_file.read()
        return json.loads(file_content)

def update_user(user: dict, uuid: str) -> str:
    with open(config.USERS_PATH + uuid, 'w') as user_file:
        user_file.write(json.dumps(user))
    return user

def delete_user(uuid: str):
    if uuid in __users_index:
        os.remove(config.USERS_PATH + uuid)
        __users_index.remove(uuid)
        with open(config.USER_FILE, 'w') as index_file:
            index_file.write(json.dumps(__users_index))
