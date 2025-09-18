# listando dados com mongoDB

from pymongo import MongoClient

client = MongoClient()

my_db = client.socialmedia 
my_collection = my_db.posts 

result = my_collection.find_one()
print(result)

all_results = my_collection.find()

# listando todos os documentos
for r in all_results:
    print(r)
