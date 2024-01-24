#!/usr/bin/env python3
"""
Sorts students by average score (Top students)
"""


def top_students(mongo_collection):
    """ returns sorted students by average score """

    pipeline = [
        {
            "$project": {
                "name": $name,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return mongo_collection.aggregate(pipeline)
