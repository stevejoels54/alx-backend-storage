#!/usr/bin/env python3
"""
lists schools having specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    list of schools having specific topic
    """
    return mongo_collection.find({"topics": topic})
