#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import myJson as myjson


class GroceryController:
    def __init__(self):
        self.filename = "json.txt"
        self.jsonObject = myjson.loadJSON("json.txt")
        self.groceryID = self.jsonObject["groceryID"] if "groceryID" in self.jsonObject else 0

    def add(self, brand, name, amount, calories, carbs, protein, fat, sugar):
        self.jsonObject["grocery"] = {
            "groveryID": self.groceryID,
            "brand": brand,
            "name": name,
            "amount": amount,
            "calories": calories,
            "carbs": carbs,
            "protein": protein,
            "fat": fat,
            "sugar": sugar
        }

        self.groceryID += 1

    def typeOut(self):
        if "grocery" in self.jsonObject:
            print(self.jsonObject["grocery"])
