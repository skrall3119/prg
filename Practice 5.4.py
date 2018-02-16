def fat_calories(fat):  # Calculates calories from fat
    return fat * 9


def carb_calories(carb):  # Calculates calories from carbohydrates
    return carb * 4


def protein_calories(protein):  # calculates calories from protein
    return protein * 4


def print_totals():  # prints out calculations and total
    print("\nthe number of calories from fat is:", fat_calories(fat_grams))
    print("The number of calories from carbohydrates is:", carb_calories(carb_grams))
    print("The number of calories from protein is:", protein_calories(protein_grams))
    print("The total number of calories is:", calories)


#  takes input from user
fat_grams = int(input("Enter the amount of grams of fat you ate: "))
carb_grams = int(input("Enter the amount of grams of carbohydrates you ate: "))
protein_grams = int(input("Enter the amount of grams of protein you ate: "))

# Calculates total calories
calories = fat_calories(fat_grams) + carb_calories(carb_grams) + protein_calories(protein_grams)
print_totals()


