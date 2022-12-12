import psycopg2
import os

conn = psycopg2.connect(database="cardanodbsync",
                        host=os.environ['DBSYNC_POSTGRESQL_HOSTNAME'],
                        user=os.environ["DBSYNC_POSTGRESQL_USER"],
                        password=os.environ["DBSYNC_POSTGRESQL_PASSWORD"],
                        port=os.environ["DBSYNC_POSTGRESQL_PORT"])

cursor = conn.cursor()