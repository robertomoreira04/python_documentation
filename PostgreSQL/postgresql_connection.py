import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)

