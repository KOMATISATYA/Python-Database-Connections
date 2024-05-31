import pymongo

client=pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["mydb"]

collection=db["example"]

docs=[
    {
        "name":"satya",
        "age":21
    },{
        "name":"siddu",
        "age":28
    }
]

result = collection.insert_many(docs)
print("The Documents are successfully inserted")
print(result.inserted_ids)