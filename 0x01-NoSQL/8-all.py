#!/usr/bin/env python3
"""Listing all docs in a collection"""


def list_all(mongo_collection):
    """
    lists documents in a collection
    """
    docs = mongo_collection.find()

    if docs.countDocuments({}) == 0:
        return []
    return docs
