#!/usr/bin/env python3

"""
this function returns all students sorted by average score
the top must be ordered
the average score must be part of each item returns
with key = averageScore
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    method definition
    """
    pipeline = [
            {
                "$addFields": {
                    "averageScore": {
                        "$avg": "$scores"
                        }
                    }
                },
            {
                "$sort": { "averageScore": -1 }
                }
            ]
    return list(mongo_collection.aggregate(pipeline))
