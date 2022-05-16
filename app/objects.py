
class User:

    def __init__(self, **kwargs):
        self.id = kwargs['id'] if 'id' in kwargs else None
        self._creation_date = kwargs['creation_date'] if 'creation_date' in kwargs else None

        self.username = kwargs['username'] if 'username' in kwargs else None
        self.password = kwargs['password'] if 'password' in kwargs else None

        self.firstname = kwargs['firstname'] if 'firstname' in kwargs else None
        self.lastname = kwargs['lastname'] if 'lastname' in kwargs else None
        self.birthdate = kwargs['birthdate'] if 'birthdate' in kwargs else None
        self.phone = kwargs['phone'] if 'phone' in kwargs else None
        self.mail = kwargs['mail'] if 'mail' in kwargs else None
        self.notes = kwargs['notes'] if 'notes' in kwargs else []

    def __json__(self):
        return {
            "id": self.id,
            "creation_date": self._creation_date,
            "username": self.username,
            "password": self.password,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone": self.phone,
            "mail": self.mail,
            "notes": self.notes,
        }

    def __repr__(self):
        return {
            'id': self.id,
            'creation_date': self._creation_date,
            'username': self.username,
            'password': self.password,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'phone': self.phone,
            'mail': self.mail,
            'notes': self.notes,
        }

    def __str__(self):
        return self.__repr__().__str__()
