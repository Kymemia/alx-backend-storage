#!/usr/bin/env python3

"""
this is a python script that provides
some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db.nginx

all_logs = collection.count_documents({})
print(f"{all_logs} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("Methods:")
for method in methods:
    """
    condition to iterate over the methods listed above
    to get the number of documents in the collection
    that have these methods
    """
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count} status check")
