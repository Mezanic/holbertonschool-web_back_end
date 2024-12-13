#!/usr/bin/env python3
""" This module define function that returns the list"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    result = mongo_collection.find(
        {"topics": topic}
    )

    return list(result)
