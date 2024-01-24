#!/usr/bin/env python3
"""
lists all documents in collection
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collection documents
    """

    if not mongo_collection:
        return []
    else:
        return list(mongo_collection.find())
