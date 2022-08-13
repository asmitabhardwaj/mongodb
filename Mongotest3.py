import pymongo
client = pymongo.MongoClient("mongodb+srv://asmitab253:Jerry1998@asmita.viwj9.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection =database["asm"]
record = collection.find()
for i in record:
    print(i)

#data = collection.find({'companyName' : 'iNeuron' })
data = collection.find({'courseOffered' :{"$gte" : "E"}})
for i in data:
    print(i)