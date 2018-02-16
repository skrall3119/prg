# the main function that prints the lowest recommended insurance payment.
def main():
    print("The minimum amount of insurance you should buy is: $" + format(calculate_insurance(get_cost()), ',.2f'))


# gets the value of the building from the user
def get_cost():
    cost = float(input("enter cost of building: "))
    return cost


# calculates the insurance cost using the value received from the user
def calculate_insurance(cost):
    insurance_cost = cost * .8
    return insurance_cost
main()
