# deletando dados com mongoDB

from pymongo import MongoClient 

client = MongoClient() 
my_db = client.socialmedia  
my_collection = my_db.posts 

query = {"category": "Banco de dados não relacional"}

x = my_collection.delete_one(query)
print(f"{x.deleted_count} documento excluído")

