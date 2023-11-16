## Run the development files
win-run:
	.\.env\Scripts\python.exe main.py

unix-run:
	.venv/bin/python3 ./main.py

# Generate database migrations
win-gen-migrations:
	.\.env\Scripts\alembic.exe revision --autogenerate

# Import docker database to work locally
import-database-snapshot:
	sudo rsync -avz --stats --delete $(whoami)@remote:~/projectname_postgres_save/ ../../projectname_postgres_data

create-database-snapshot:
	sudo rsync -av --no-perms --delete --chown=$(whoami) ../../projectname_postgres_data/ ../../projectname_postgres_save
	sudo chown -R $(whoami):$(whoami) ../../projectname_postgres_save
