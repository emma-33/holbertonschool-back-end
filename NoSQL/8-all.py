#!/usr/bin/env python3
"""Defines a function that lists all documents in a collection """


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    if mongo_collection is None:
        return []
    else:
        documents = mongo_collection.find()
        return documents
