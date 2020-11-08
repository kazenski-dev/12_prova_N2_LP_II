from pymongo import MongoClient

class MongoConnect():

    def save(self, json):
        try:
            conectar = MongoClient('localhost', 27017)
            banco = conectar.prova 
            col_musica = banco.musica
            id = col_musica.insert_one(json).inserted_id
        except Exception as e:
            print("Problema ao salvar registro.")
            print(json)
            print(e)
