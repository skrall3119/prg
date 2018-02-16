def fatCalories(fat): # Calculates calories from fat
    return fat * 4


def carbCalories(carb): # Calculates calories from carbohydrates
    return carb * 4


def proteinCalories(protein): # calculates calories from protein
    return protein * 4


def printTotals():# prints out calculations and total
    print("\nthe number of calories from fat is:", fatCalories(fatGrams))
    print("The number of calories from carbohydrates is:", carbCalories(carbGrams))
    print("The number of calories from protein is:", proteinCalories(proteinGrams))
    print("The total number of calories is:", calories)

calories = 0 # initialize total calorie count

 # takes input from user
fatGrams = int(input("Enter the amount of grams of fat you ate: "))
carbGrams = int(input("Enter the amount of grams of carbohydrates you ate: "))
proteinGrams = int(input("Enter the amount of grams of protein you ate: "))

# Calculates total calories
calories = fatCalories(fatGrams) + carbCalories(carbGrams) + proteinCalories(proteinGrams)
printTotals()


