# Templates-backend

Technologies
* Docker deployment
* Postgresql database
* SQLAlchemy ORM
* Alembic database migrations
* Strawberry GraphQL
* FastAPI Web Framework
* Uvicorn server

## Setup

- Create `./docker.env` file with as structure similar to `./docker.example.env`
- Create `./src/settings.ini` file with a structure similar to `./src/settings.example.ini`
- Rename all `projectname` string to the name of your choice on all file/file-names.

## Prod

Use the `deploy.sh` script to get the latest version of code and refresh the docker containers.

## Dev

- Set the database similar to prod using a docker container

```docker compose -f docker-compose-dev.yaml --env-file docker.env up projectname-postgres```


### Virtual environment

In `./src/`, set your virtual environment according to your machine:

#### Windows Python

```
python -m venv .env
.\.env\Scripts\python.exe -m pip install --upgrade pip
.\.env\Scripts\python.exe -m pip install -r .\requirements.txt
"$(get-location)" > .\.env\Lib\site-packages\obugs.pth
```

#### Unix Python

```
python3 -m venv .venv
.venv/bin/pip3 install --upgrade pip
.venv/bin/pip3 install -r requirements.txt
$(foreach dir, $(wildcard .venv/lib/*), echo $(shell pwd) > $(dir)/site-packages/obugs.pth &&) echo
```

### Run

- Windows: ``.\.env\Scripts\python.exe main.py``
- Unix: ``.venv/bin/python3 ./main.py``

### Generate a new database migration

- Windows: ``.\.env\Scripts\alembic.exe revision --autogenerate``
- Unix: ``.venv/bin/alembic revision --autogenerate``

More scripts in ``./src/Makefile``
