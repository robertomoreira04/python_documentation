# lendo dados em sqlite 

import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute("SELECT name, year FROM movies")
data = cursor.fetchall()  
print(data)

for row in cursor.execute("SELECT * FROM movies"):
    print(f'{row}')

# ordenando pelo nome dos filmes
for row in cursor.execute("SELECT * FROM movies ORDER BY name"):
    print(f'{row}')

connection.close()

