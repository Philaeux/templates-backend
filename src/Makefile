#######################################
#        Windows environment          #
#######################################

## Create a.py virtual environment and install dependencies
win-install:
	python -m venv .env
	.\.env\Scripts\python.exe -m pip install --upgrade pip
	.\.env\Scripts\python.exe -m pip install -r .\requirements.txt
	"$(get-location)" > .\.env\Lib\site-packages\projectname.pth

win-run:
	.\.env\Scripts\python.exe main.py

## Remove development environment
win-clean:
	rm -r .\.env\

# Generate database migrations
win-gen-migrations:
	.\.env\Scripts\alembic.exe revision --autogenerate


#######################################
#          Unix environment           #
#######################################

## Create a.py virtual environment and install dependencies
unix-install:
	python3 -m venv .venv
	.venv/bin/pip3 install --upgrade pip
	.venv/bin/pip3 install -r requirements.txt
	$(foreach dir, $(wildcard .venv/lib/*), echo $(shell pwd) > $(dir)/site-packages/projectname.pth &&) echo

## Run the development files
unix-run:
	.venv/bin/python3 ./main.py

## Remove development environment
unix-clean:
	rm -rf .venv

import-database-snapshot:
	sudo rsync -avz --stats --delete $(whoami)@remote:~/projectname_postgres_save/ ../../projectname_postgres_data

create-database-snapshot:
	sudo rsync -av --no-perms --delete --chown=$(whoami) ../../projectname_postgres_data/ ../../projectname_postgres_save
	sudo chown -R $(whoami):$(whoami) ../../projectname_postgres_save

