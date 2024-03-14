FastAPI
========

Periodic Tasks
---------------

It's possible to create periodic tasks. Use this function decorator:
    
.. autofunction:: template.utils.repeat_every.repeat_every

And then call this function in the lifecycle function:

.. autofunction:: template.backend.lifecycle

GraphQL
--------

Schema
^^^^^^^

Schema defined for the GraphQL endpoint:

.. automodule:: template.graphql.schema
    :members:

Types Input & Output
^^^^^^^^^^^^^^^^^^^^^^

I recommend creating files to store Input and Output types of the GraphQL endpoints, in files like ``src/template/graphql/types/a.py``.

These types are used:

.. automodule:: template.graphql.types.generic
    :members:


Generated Types
^^^^^^^^^^^^^^^^

These types are generated from ORM objects. When a query/mutation return an ORM type, it's automaticaly turned into a GraphQL type.

.. automodule:: template.graphql.types.generated
    :members:

REST API
----------

It is possible to create classic REST endpoints instead of using the GraphQL endpoint. A demonstration function is:

.. autofunction:: template.backend.hello

I recommend using REST for the OAuth process, using 2 functions ``oauth_login`` and ``oauth_callback`` per provider (Google, Reddit...).
