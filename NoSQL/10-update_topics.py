"""Module define a function for change topics"""


def update_topics(mongo_collection, name, topics):
    """"Changes all topics of a school document based on the name """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
