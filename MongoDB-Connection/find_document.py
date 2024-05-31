import pymongo

client=pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client['mydb']

collection=db["example"]

print("find one...",collection.find_one())

for doc in collection.find():
    print("docs..",doc)


print(collection.find_one({"name":"satya"}))


for doc in collection.find({"age":{"$gt":26}}):
    print(doc)