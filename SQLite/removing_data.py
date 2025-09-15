# removendo dados em sqlite 

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

id = int(input("Informe o id do filme que deseja remover:\n>"))

cursor.execute("""
        DELETE FROM movies 
        WHERE id = ?
            """, (id,)) # atenção à vírgula para criar uma tupla

connection.commit()
print("Filme removido com sucesso!")

connection.close()