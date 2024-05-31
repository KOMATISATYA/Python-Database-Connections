import pymongo

client=pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db=client["mydb"]

collection=db['example']


collection.update_many({}, {"$set": {"age" : 20}})
print("Updated Successfully")

for doc in collection.find():
    print(doc)