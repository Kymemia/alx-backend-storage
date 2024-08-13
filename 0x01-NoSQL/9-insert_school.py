#!/usr/bin/env python3

"""
this function inserts a new document
in a collection based on kwargs
and returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    method definition
    """
    end_product = mongo_collection.insert_one(kwargs)
    return end_product.inserted_id
