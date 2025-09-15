# inserindo dados em sqlite com input e parametrização 

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

name = input("Nome do filme\n")
year = int(input("Ano do filme\n"))
score = float(input("Nota do filme\n"))

cursor.execute("""
        INSERT INTO movies (name, year, score)
        VALUES (?, ?, ?)
                """, (name, year, score))

connection.commit()
print("Dados inseridos com sucesso")

connection.close()
