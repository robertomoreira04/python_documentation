# inserindo dados com mongoDB

from pymongo import MongoClient 

client = MongoClient() # cria conexão com o mongodb da máquina

my_db = client.socialmedia # criando o banco de dados 
my_collection = my_db.posts # criando a coleção

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