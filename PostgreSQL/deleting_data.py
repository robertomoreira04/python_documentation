# deletando dados em postgreSQL

from postgresql_connection import conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM game
    WHERE id = %s
"""

cursor_obj.execute(sql, (4,))

conn.commit()

print("Dado removido com sucesso")

conn.close()