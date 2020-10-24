

def addGrocery(gcObj):
    brand = input("Brand:")
    name = input("Name:")
    amount = input("Amount:")

    print("Enter nutritional values:")
    calories = input("Calories:")
    carbs = input("Carbohydrates:")
    protein = input("Protein:")
    fat = input("Fat:")
    gcObj.add(brand, name, amount, calories, carbs, protein, fat, sugar)

    # Verbose
    print(calories)
    print(carbs)
    print(protein)
    print(fat + "\n")
