from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["film_db"]
collection = db["contents"]

# the data you want to add
data_list = [
    {
        "title" : "Sample Content 1",
        "year" : 2023,
        "length" : 120,
        "producer" : "Sample Producer 1",
        "description" : "This is a sample content 1.",
        "genre" : ["Action", "Adventure"],
    },
    {
        "title": "Sample Content 2",
        "year": 2023,
        "length": 90,
        "producer": "Sample Producer 2",
        "description": "This is a sample content 2.",
        "genre": ["Drama", "Romance"],
    },
    #Other data you want to add...
]

# add data to MongoDB
result = collection.insert_many(data_list)

#print the IDs of the attached documents
print(f"Inserted documents IDs: {result.inserted_ids}")

