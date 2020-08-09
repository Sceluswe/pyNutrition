#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import saveToJSON as save

#
# Global default settings
#
EXIT_SUCCESS = 0

def main():
    jsonObj = save.loadJSON("json.txt");
    print("Enter nutritional values:")
    calories = input("Calories:")
    carbs = input("Carbohydrates:")
    protein = input("Protein:")
    fat = input("Fat:")

    print(calories)
    print(carbs)
    print(protein)
    print(fat)
    sys.exit(EXIT_SUCCESS)

main()
