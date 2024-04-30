#!/usr/bin/env python3
"""Defines a function that changes all topics of a school document based
on the name"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school based on the name"""

    new_name = {"name": name}
    new_topics = {"$set": {"topics": topics}}

    updated_school = mongo_collection.update_many(new_name, new_topics)

    return updated_school
