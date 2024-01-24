#!/usr/bin/env python3
"""
inserts new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert document into mongo_collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
