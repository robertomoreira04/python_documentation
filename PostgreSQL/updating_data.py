# inserindo dados em postgreSQL


from postgresql_connection import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE game 
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ("FIFA 25", 4))

conn.commit()
print("Dados atualizados")
conn.close()