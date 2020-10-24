#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Save jsonObj to json file.
"""
import json

def loadJSON(filename):
    """
    Load a JSON file.
    Return JSON object.
    """
    returnObj = None

    # Try to create the file, if it exists just move on.
    try:
        with open(filename, "x") as JSONfile:
            json.dump({}, JSONfile, indent=4)
    except FileExistsError:
        pass
    # Load the JSON file.
    with open(filename, "r") as JSONfile:
        returnObj = json.load(JSONfile)

    return returnObj


def saveJSON(filename, JSONobject):
    """
    Take a sequence and save it as JSON.
    """
    # Try to create the file, if it exists just move on.
    try:
        open(filename, "x")
    except FileExistsError:
        pass
    # Save the sequence to the file.
    with open(filename, "w") as JSONfile:
        json.dump(JSONobject, JSONfile, indent=4)


# test code:
loadJSON("json.txt")
# Create a dictionary
my_dict = {"lel": "test", "nej": "test1"}
# Save dictionary in a dict called seo
jsonObj = {"seo": my_dict}
# make it a json object and dump it to a file.
