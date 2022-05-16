
import uuid
import datetime
from app.nosql import Table, Query
from app.objects import User
from app.validators import _create_validator, _update_validator


class Domain:
    def __init__(self):
        self._users_db = Table('users')

    def register(self, **payload):
        pass

    def login(self, **payload):
        pass

    def create_user(self, **obj_to_create):
        obj_to_create['creation_date'] = datetime.datetime.now().strftime("%Y-%m-%d")
        obj_to_create['id'] = uuid.uuid4().__str__()
        new_user = User(**obj_to_create)

        can = _create_validator(new_user)
        if can == 200:
            self._users_db.insert(new_user.__repr__())
        return can

    def read_user(self):
        return self._users_db.all()

    def read_user_by_id(self, id):
        q = Query()
        return self._users_db.search(q.id == id)

    def update_user(self, id,  **obj_to_update):
        q = Query()
        user_found = self._users_db.search(q.id == id)
        if len(user_found) == 0:
            return 'No user found.'

        upt_user = User(**obj_to_update)

        can = _update_validator(upt_user)
        if can == 200:
            self._users_db.insert(upt_user.__repr__())
        return can

    def delete_user(self, id):
        q = Query()
        self._users_db.remove(q.id == id)
