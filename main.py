#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import GroceryController as gc

#
# Global default settings
#
EXIT_SUCCESS = 0

def main():
    gcObj = gc.GroceryController()

    print("1. Create grocery")
    print("2. Create portion")
    print("3. Create meal")

    print("Enter nutritional values:")
    calories = input("Calories:")
    carbs = input("Carbohydrates:")
    protein = input("Protein:")
    fat = input("Fat:")

    print(calories)
    print(carbs)
    print(protein)
    print(fat + "\n")

    gcObj.add(calories, carbs, protein, fat, "0")
    gcObj.typeOut()

    sys.exit(EXIT_SUCCESS)

main()
