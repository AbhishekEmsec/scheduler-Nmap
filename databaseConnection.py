import pymongo

# MongoDb Connection...
client =pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
db =client['']
collection =db['']
print ("total docs in collection:", collection.count_documents( {} ))



