import pymongo

client=pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["mydb"]
collection=db["example"]

print("collection created...")

print("collection list..", db.list_collection_names())