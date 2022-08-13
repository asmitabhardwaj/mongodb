import pymongo
client = pymongo.MongoClient("mongodb+srv://asmitab253:Jerry1998@asmita.viwj9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" :"Asmita",
    "email" :"asmitab253@gmail.com",
    "surname" :"Kumari",
    "age" : "25"
    }
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)