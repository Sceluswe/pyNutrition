#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import jsonFoodWrapper as jfw

#
# Global default settings
#
EXIT_SUCCESS = 0

def main():
    jfwObj = jfw.jsonFoodWrapper()

    print("Enter nutritional values:")
    calories = input("Calories:")
    carbs = input("Carbohydrates:")
    protein = input("Protein:")
    fat = input("Fat:")

    print(calories)
    print(carbs)
    print(protein)
    print(fat + "\n")

    jfwObj.add(calories, carbs, protein, fat, "0")
    jfwObj.typeOut()

    sys.exit(EXIT_SUCCESS)

main()
