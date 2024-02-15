import configparser
from pathlib import Path

from template.utils.singleton_meta import SingletonMeta


class Settings(metaclass=SingletonMeta):
    """Parameters of the application read from settings.ini
    
    Attributes:
        debug: Flag to set debug options in all application
        jwt_secret_key: secret to generate JWTs
        database_uri: URI to connect to the database
        frontend_uri: URI to the frontend related to this app (to redirect auth)
        backend_uri: URI this backend is accessed from
    """
    debug: bool = True
    jwt_secret_key: str = "sssssssss"
    database_uri: str = "postgresql+psycopg://template:sssssssss@host.docker.internal:5432/template"
    frontend_uri: str = "http://127.0.0.1:4200"
    backend_uri: str = "http://127.0.0.1:5000"

    def __init__(self):
        """Lis le fichier de configuration depuis le fichier settings.ini"""
        cfg = configparser.ConfigParser()
        cfg.read(Path(__file__).parent / ".." / "settings.ini")

        self.debug = cfg['DEFAULT'].getboolean('debug', fallback=self.debug)
        self.jwt_secret_key = cfg['DEFAULT'].get('jwt_secret_key', fallback=self.jwt_secret_key)
        self.database_uri = cfg['DEFAULT'].get('database_uri', fallback=self.database_uri)
        self.frontend_uri = cfg['DEFAULT'].get('frontend_uri', fallback=self.frontend_uri)
        self.backend_uri = cfg['DEFAULT'].get('backend_uri', fallback=self.backend_uri)
