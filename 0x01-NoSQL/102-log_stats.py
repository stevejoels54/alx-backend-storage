#!/usr/bin/env python3
"""Defines a function that provides stats
   about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats_check():
    """gives stats about Nginx logs stored in MongoDB"""

    client = MongoClient()
    mongo_collection = client.logs.nginx

    total_logs = mongo_collection.count_documents({})
    methods_count = {
        "GET": mongo_collection.count_documents({"method": "GET"}),
        "POST": mongo_collection.count_documents({"method": "POST"}),
        "PUT": mongo_collection.count_documents({"method": "PUT"}),
        "PATCH": mongo_collection.count_documents({"method": "PATCH"}),
        "DELETE": mongo_collection.count_documents({"method": "DELETE"})
    }

    status_check_count = mongo_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    top_ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")

    print(f"{status_check_count} status check")

    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    nginx_stats_check()
