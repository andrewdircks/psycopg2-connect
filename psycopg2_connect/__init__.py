import os
import logging
import psycopg2

def connect():
    # get db credentials from environment
    try:
        user = os.environ['db_user']
        host = os.environ['db_host']
        port = os.environ['db_port']
        database = os.environ['db_name']
        password = os.environ['db_password']
    except:
        logging.error(f'error getting environment. missing one of \
            db_user, db_host, db_port, db_name, db_password env vars')
        raise Exception('environment not configured')

    # connect
    try: 
        return psycopg2.connect(user=user, 
                                host=host, 
                                port=port, 
                                database=database,
                                password=password)
    except:
        logging.error(f'error connecting to database. current environment:\
            user {user}, host: {host}, port: {port}, database: {database}, password: {password}.')
        raise Exception('database connection error, see logs.')
