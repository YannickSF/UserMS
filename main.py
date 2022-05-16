
from app.endpoints import app


class _Setting:
    NAME = 'UserMS'
    HOST = '0.0.0.0'
    PORT = 5000


SETTINGS = _Setting()


if __name__ == '__main__':
    app.run(host=SETTINGS.HOST, port=SETTINGS.PORT)
