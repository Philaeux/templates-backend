import configparser
import os
from pathlib import Path

from projectname.helpers import SingletonMeta


class Settings(metaclass=SingletonMeta):
    debug: bool = False
    database_uri: str = ''
    jwt_secret_key: str = 'super-secret'

    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read(Path(os.path.dirname(__file__)) / ".." / "settings.ini")

        self.debug = cfg['DEFAULT'].getboolean('debug', fallback=self.debug)
        self.database_uri = cfg['DEFAULT'].get('database_uri', fallback=self.database_uri)
        self.jwt_secret_key = cfg['DEFAULT'].get('jwt_secret_key', fallback=self.jwt_secret_key)
