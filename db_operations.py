from pymongo import MongoClient

def db_connection(db_location,db_name,db_collection):
    # Connect to MongoDB
    client = MongoClient(db_location)
    db = client[db_name]
    collection = db[db_collection]
    print("db bağlantısı sağlandı")
    return collection

@db_connection
def db_create():
    collection.insert_many(habbo_futured.to_dict('records'))

@db_connection
def db_insert():
    collection.insert_many(habbo_futured.to_dict('records'))

@db_connection
def db_delete():
    collection.delete_many({})

db_location = "mongodb+srv://uca_user:uca275790@miscluster.e0wxb.mongodb.net/MisDatabase?retryWrites=true&w=majority"
collection = "Mis"


