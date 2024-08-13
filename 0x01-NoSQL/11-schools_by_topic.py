#!/usr/bin/env python3

"""
this function returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    method definition
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)
