import pymongo

client = pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['mydb']

collection = db['example']

print("The Collections before dropping :")

for coll in db.list_collection_names():
    print(coll)
print("\n")

collection.drop()
print("The Collection is dropped from the Database..!")

print("The Collections list after dropping :")

for coll in db.list_collection_names():
    print(coll)