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
    programLoop = True
    gcObj = gc.GroceryController()

    print("0. Exit")
    print("1. Create grocery")

    #print("2. Create portion")
    #print("3. Create meal")

    while(programLoop):
        number = input("Menu Option: ")

        if number == "1":
            print("Lol")
            menu.addGrocery(gcObj)
        if number == "0":
            programLoop = False

    gcObj.typeOut()

    sys.exit(EXIT_SUCCESS)


main()
