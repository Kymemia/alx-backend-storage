#!/usr/bin/env python3

"""
this function changes all topics of a school document
based on the name
Args:
    name(string) will be the school name to update
    topics(list of strings) will be the list
    of topics approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    method definition
    """
    end_product = mongo_collection.update_one(
            {"name": name},
            {"$set": {"topics": topics}}
            )
    return end_product.modified_count
