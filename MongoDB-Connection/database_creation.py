import pymongo

client=pymongo.MongoClient("mongodb+srv://komatisatya1919:Satya1919@cluster0.zwimdqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["mydb1"]
print(db)
print("Database created successfully.")
collection = db["mycollection"]
collection.insert_one({"example_key": "example_value"})

# Fetch The List of Databases from the Client
print("The List of Databases : \n", client.list_database_names())