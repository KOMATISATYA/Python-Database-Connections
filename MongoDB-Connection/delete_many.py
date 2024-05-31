from pymongo import MongoClient

client=MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client['mydb']

collection=db['example']

collection.delete_many({"name":"satya"})

collection.delete_many({"age" : {"$lt" : 20}})

for doc in collection.find():
    print(doc)