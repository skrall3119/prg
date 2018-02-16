def main(): #The main function that gets the input from the user and prints out the costs per month and costs per year
    loan = int(input("Enter your monthly loan payment: "))
    insurance = int(input("Enter your monthly insurance payment: "))
    gas = int(input("Enter the amount you spend on gas monthly: "))
    tires = int(input("Enter the amount you spend on tires monthly: "))
    maintenance = int(input("Enter the cost to maintain your vehicle: "))

    monthlyCosts = addCosts(loan, insurance, gas, tires, maintenance)
    yearlyCosts = calculateYearlyCost(monthlyCosts)
    printCosts(yearlyCosts, monthlyCosts)


def addCosts(a, b, c, d, e): #adds the amounts given by the user
    monthlytotal = a + b + c + d + e
    return int(monthlytotal)

def calculateYearlyCost(monthlytotal): #calculates the yearly cost with the value returned by addCosts
    yearlyCost = monthlytotal * 12
    return yearlyCost

def printCosts(yearlyCost, monthlyCost): #prints the costs calculated in addCosts and calculateYearlyCost
    print("The monthly total for your vehicle is:", format(monthlyCost, ',.2f'))
    print("The yearly total for your vehicle is:", format(yearlyCost, ',.2f'))

main()
