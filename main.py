#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import GroceryController as gc
import menu

#
# Global default settings
#
EXIT_SUCCESS = 0

def main():
    gcObj = gc.GroceryController()

    print("1. Create grocery")
    #print("2. Create portion")
    #print("3. Create meal")

    number = input("Menu Option: ")

    switch(number)
    {
        case 1:
        menu.addGrocery(gcObj)
        break;
        default:
        printf("Option doesn't exist.")
    }

    gcObj.typeOut()

    sys.exit(EXIT_SUCCESS)

main()
