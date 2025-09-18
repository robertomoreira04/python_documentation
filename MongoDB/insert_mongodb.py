# inserindo dados com mongoDB

from pymongo import MongoClient 

client = MongoClient() 

my_db = client.socialmedia  
my_collection = my_db.posts 

post1 = {
    "title": "Learning MongoDB",
    "category": "Banco de Dados",
    "author": {
        "name": "Roberto",
        "email": "robertodev04@gmail.com"
    }
}

result = my_collection.insert_one(post1)
print("Documento adicionado com sucesso!")