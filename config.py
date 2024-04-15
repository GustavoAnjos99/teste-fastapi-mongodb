import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017")

database = cliente['teste-python']
collection = database['collection-teste']

lista_de_dados = [
    {"nome": "gustavo"},
    {"nome": "nelson"},
    {"nome": "roberta"},
    {"nome": "lais"}
]

# CRUD:

collection.insert_many(lista_de_dados)
collection.find()
collection.update_one( {"nome": "nelson"} , {"$set": {"nome": "NeLsOn"}} )
collection.delete_one( {"nome": "gustavo"} )
