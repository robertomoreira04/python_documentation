# inserindo dados em postgreSQL


from postgresql_connection import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars Survivor', 2023, 9.0),
    ('Luigis Mansion 3', 2019, 9.0),
]

for game in games:
    cursor_obj.execute("""
            INSERT into game(name, year, score)
            VALUES (%s, %s, %s)

                    """, game)
    
conn.commit()

print("Dados inseridos")

conn.close()