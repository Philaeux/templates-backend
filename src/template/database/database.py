import os
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from template.database.base import Base


class Database:
    """Singleton defining database URI and unique ressources.

    Attributes:
        _instance: Singleton instance
        uri: database location
        engine: database connection used for session generation
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """New overload to create a.py singleton."""
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, uri='', auto_migrate=False):
        """Defines all necessary ressources (URI & engine) and create database if necessary."""

        dir_uri = os.path.dirname(__file__)
        if uri == '':
            self.uri = f"sqlite+pysqlite:///{dir_uri}/sqlite.db"
        else:
            self.uri = uri
        self.engine = create_engine(self.uri, echo=False)
        self.session_factory = sessionmaker(self.engine)

        # Upgrade application to heads
        if auto_migrate:
            alembic = Path(dir_uri) / ".." / ".." / "alembic.ini"
            migrations = Path(dir_uri) / ".." / "alembic"
            alembic_cfg = Config(alembic)
            alembic_cfg.set_main_option('script_location', str(migrations))
            alembic_cfg.set_main_option('sqlalchemy.url', self.uri)
            command.upgrade(alembic_cfg, 'head')
