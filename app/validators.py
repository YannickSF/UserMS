
from jsonschema import ValidationError, validate

user_register = {
    "type": "object",
    "properties": {
        "mail": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
    }
}

user_login = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    }
}

user_create_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "date_creation": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "mail": {"type": "string"},

    }
}

user_update_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "date_creation": {"type": "string"},
        "username": {"type": "string"},
        "password": {"type": "string"},
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "birthdate": {"type": "string"},
        "phone": {"type": "string"},
        "mail": {"type": "string"},
        "notes": {"type": "string"}
    }
}


def _register_validator(object_to_create):
    try:
        validate(instance=object_to_create.__json__(), schema=user_register)
        return 200
    except ValidationError as ve:
        return ve.message


def _login_validator(object_to_create):
    try:
        validate(instance=object_to_create.__json__(), schema=user_login)
        return 200
    except ValidationError as ve:
        return ve.message


def _create_validator(object_to_create):
    try:
        validate(instance=object_to_create.__json__(), schema=user_create_schema)
        return 200
    except ValidationError as ve:
        return ve.message


def _update_validator(object_to_update):
    try:
        validate(instance=object_to_update.__json__(), schema=user_update_schema)
        return 200
    except ValidationError as ve:
        return ve.message
