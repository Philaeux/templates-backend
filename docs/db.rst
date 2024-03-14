Database
==========

ORM: Object Relational Mapping
-------------------------------

ORM classes are used to map the database to python objects.

.. mermaid::
    classDiagram
        A: +Int id

.. automodule:: template.database.a
    :members:

To use the database, we use the Database singleton.

.. autoclass:: template.database.database.Database
    :members:

Migrations
-----------

To generate a new database migration (new tables, new columns, deletions, updates...), change the ORM classes first. 
Then, generate the new migration using Alembic::

    poetry run alembic revision --autogenerate

A new migration will appear in ``src/template/alembic/versions``. Update the file accordingly.

It's possible to decide if migrations are automaticaly run at startup. Otherwise, use manual updates::

    # Forward
    poetry run alembic revision +1
    # Backward
    poetry run alembic revision -1
