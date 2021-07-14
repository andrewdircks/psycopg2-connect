# GFunction Auth

Connect to postgres servers using `psycopg2`.

## Install

`pip install psycopg2-connect`

## Usage

```
from psycopg2_connect import connect
conn = connect(user, host, port, database, password)
```