# criando banco de dados sqlite 

import sqlite3

connection = sqlite3.connect("movies.db")

print(connection.total_changes)

