#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import myJson as myjson


class jsonFoodWrapper:
    def __init__(self):
        self.filename = "json.txt"
        self.jsonObject = myjson.loadJSON("json.txt")
        self.groceryID = self.jsonObject["groceryID"] if "groceryID" in self.jsonObject else 0
        print(self.groceryID)

    def add(self, calories, carbs, protein, fat, sugar):
        self.jsonObject["grocery"] = {
            "calories": calories,
            "carbs": carbs,
            "protein": protein,
            "fat": fat,
            "sugar": sugar
        }

    def typeOut(self):
        print(self.jsonObject["grocery"])
