import psycopg2

conn = psycopg2.connect(database="cardanodbsync",
                        host="",
                        user="",
                        password="",
                        port="")

cursor = conn.cursor()