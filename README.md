# forest_backend

# Installation
## Flask
pip install -r requirements.txt

## Postgres
brew install postgres
initdb /usr/local/var/postgres
createdb forest
pg_ctl -D /usr/local/var/postgres -l logfile start


# Running 
## Flask
python run.py

## Postgres
psql forest
or
psql postgres

\list: lists all the databases in Postgres
\connect: connect to a specific database
\dt: list the tables in the currently connected database

## SQLAlchemy
python migrate.py db init

### apply migrations
python migrate.py db migrate
python migrate.py db upgrade

# Tutorial
https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx
https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d

