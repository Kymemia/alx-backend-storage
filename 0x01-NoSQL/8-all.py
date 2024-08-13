#!/usr/bin/env python3

"""
this function lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    method collection
    """
    documents = list(mongo_collection.find())

    return documents if documents else []
