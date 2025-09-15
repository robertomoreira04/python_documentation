# inserindo dados de forma direta no sqlite


import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute("""

        INSERT INTO movies (name, year, score)
        VALUES ('Super Mario Bros', 2023, 10)
                """)

cursor.execute("""

        INSERT INTO movies (name, year, score)
        VALUES ('Avatar', 2023, 9.5)
                """)

cursor.execute("""

        INSERT INTO movies (name, year, score)
        VALUES ('Velozes e furiosos 10', 2023, 8.5)
                """)

connection.commit()
print("Dados inseridos com sucesso")

connection.close()


