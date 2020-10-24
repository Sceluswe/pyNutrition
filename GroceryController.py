#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import myJson as myjson


class GroceryController:
    def __init__(self):
        self.filename = "json.txt"
        self.jsonObject = myjson.loadJSON("json.txt")
        self.groceryID = self.jsonObject["groceryID"] if "groceryID" in self.jsonObject else 0
        print(self.groceryID)

    def add(self, brand, name, calories, carbs, protein, fat, sugar):
        self.jsonObject["grocery"] = {
            "groveryID": self.groceryID,
            "brand": brand,
            "name": name,
            "calories": calories,
            "carbs": carbs,
            "protein": protein,
            "fat": fat,
            "sugar": sugar
        }

        groceryID++;

    def typeOut(self):
        print(self.jsonObject["grocery"])
