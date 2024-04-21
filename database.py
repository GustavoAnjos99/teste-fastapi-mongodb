from pymongo import MongoClient
from bson.objectid import ObjectId


MONGO_CONNECTION_STRING = MongoClient("mongodb://localhost:27017")
database = MONGO_CONNECTION_STRING['teste-python']
collectionTeste = database['collection-teste']

async def create_usuario(usuarioJSON : dict):
    collectionTeste.insert_one(usuarioJSON) 

async def delete_usuario(id: str):
    usuario = collectionTeste.find_one( {'_id': ObjectId(id)} )
    if usuario:
        collectionTeste.delete_one( {'_id': ObjectId(id)} )
    return True


