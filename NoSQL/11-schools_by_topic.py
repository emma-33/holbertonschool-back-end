#!/usr/bin/env python3
"""Defines a function that returns the list of school having
a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""

    school_list = []
    topics = mongo_collection.find({"topics": topic})

    for schools in topics:
        school_list.append(schools)

    return school_list
