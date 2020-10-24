

def addGrocery(gcObj):
    print("Enter all values for the grocery:")
    brand = input("Brand:")
    name = input("Name:")
    amount = input("Amount:")


    calories = input("Calories:")
    carbs = input("Carbohydrates:")
    protein = input("Protein:")
    fat = input("Fat:")
    sugar = input("Sugar:")
    gcObj.add(brand, name, amount, calories, carbs, protein, fat, sugar)

    # Verbose
    print(calories)
    print(carbs)
    print(protein)
    print(fat + "\n")
