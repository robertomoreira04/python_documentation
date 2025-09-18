# atualzando dados com mongoDB

from pymongo import MongoClient

client = MongoClient()

my_db = client.socialmedia 
my_collection = my_db.posts 

old_value = { "category": "Banco de Dados" }
new_value = { "$set":{ "category": "Banco de dados não relacional"}}

my_collection.update_one(old_value, new_value)

for x in my_collection.find():
    print(x)