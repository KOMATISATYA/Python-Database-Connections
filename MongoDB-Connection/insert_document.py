from pymongo import MongoClient

client=MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client["mydb"]

collection=db["example"]

doc={
    "name":"satya",
    "age":21,
    "city":"Rajahmundry"
}

collection.insert_one(doc)

print("inserted..")
print(collection.find_one())