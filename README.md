# Psycopg2 Connect

Connect to postgres servers using `psycopg2`.

## Install

`pip install psycopg2-connect`

## Usage

Ensure environment is set up as:
```
db_host="12.34..."
db_port="5432"
db_name=example_db
db_user=example_user
db_password=example_password
```
Connect with:
```
from psycopg2_connect import connect
conn = connect()
```