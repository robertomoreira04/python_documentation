# atualizando dados em sqlite 

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

id = int(input("Informe o ID do filme (1 a 4):\n>"))
name = input("Informe o novo nome do filme:\n>")

cursor.execute("""
        UPDATE movies set name = ?
        WHERE id = ?
                """, (name, id))


connection.commit()
print("Dados atualizados com sucesso!")

connection.close()
