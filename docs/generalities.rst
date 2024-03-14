Generalities
============

Design
--------

.. mermaid::
    sequenceDiagram
        participant Client
        participant FastAPI
        participant Strawberry
        participant Database
        FastAPI ->> FastAPI: Init<br />DB Migrations<br />Periodic Start<br />Open Port
        loop Backup Périodiquement
            FastAPI ->> FastAPI: Periodic Run
        end
        Client ->> FastAPI: Query/Mutation GraphQL on "/graphql"
        FastAPI ->> Strawberry: Send GraphQL request
        Strawberry ->> Database: Execute SQL using SQLAlchemy
        Database ->> Strawberry: ORM Object response
        Strawberry ->> FastAPI: Forward response
        FastAPI ->> Client: Send JSON (ORM turned into GraphQLObjects serialized to JSON)
        Client ->> FastAPI: or REST GET/POST
        FastAPI ->> Database: Execute SQL with SQLAlchemy
        Database ->> FastAPI: ORM Object response
        FastAPI ->> Client: Send JSON (manualy define ORM -> JSON conversion)


Configuration
---------------

The backend use configuration files.

- Create ``./docker/docker.env`` similar to ``./docker/docker.example.env``. This file define database passwords for deployment or developement usign docker database. It's possible to skip this file if you prefer using a SQLite database in development.
- Create ``./src/settings.ini`` similar to ``./src/settings.example.ini``. This file defines application settings: debug mode, database access, key secrets... In development, and with SQLite, it's possible to skip the file entirely.

Run
-----

Run the backend using::

    poetry run python main.py

If you set some script, run it the same way::

    poetry run python scripts.py --help

Deploy
--------

- Stop current service::

    cd docker
    docker compose --env-file docker.env down

- Fetch changes::

    # If you want a specific tag
    git fetch origin
    git checkout v3.0.1
    # Latest code
    git pull

- Restart::

    cd docker
    docker compose --env-file docker.env up -d --build
