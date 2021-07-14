import logging
import psycopg2

def connect(user, host, port, database, password):
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