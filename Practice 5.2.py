def main():  # The main function that gets the input from the user and prints out the costs per month and costs per year
    loan = int(input("Enter your monthly loan payment: "))
    insurance = int(input("Enter your monthly insurance payment: "))
    gas = int(input("Enter the amount you spend on gas monthly: "))
    tires = int(input("Enter the amount you spend on tires monthly: "))
    maintenance = int(input("Enter the cost to maintain your vehicle: "))

    monthly_costs = add_costs(loan, insurance, gas, tires, maintenance)
    yearly_costs = calculate_yearly_cost(monthly_costs)
    print_costs(yearly_costs, monthly_costs)


def add_costs(a, b, c, d, e):  # adds the amounts given by the user
    monthly_total = a + b + c + d + e
    return int(monthly_total)


def calculate_yearly_cost(monthly_total):  # calculates the yearly cost with the value returned by add_costs
    yearly_cost = monthly_total * 12
    return yearly_cost


def print_costs(yearly_cost, monthly_cost):  # prints the costs calculated in add_costs and calculate_yearly_cost
    print("The monthly total for your vehicle is:", format(monthly_cost, ',.2f'))
    print("The yearly total for your vehicle is:", format(yearly_cost, ',.2f'))

main()
