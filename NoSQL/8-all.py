"""Script for list all document in collection"""


def list_all(mongo_collection):
    """List all document in collection"""
    if mongo_collection is None:
        return []
    else:
        return list(mongo_collection.find())
