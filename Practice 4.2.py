days = int(input("How many days will you work for pennies a day? "))
amount = 0.01
multi = 0.02
total = 0
print("\nDays worked | Amount Earned")
print("---------------------------")
for count in range(1, days + 1):
    print(format(count, '6'), "     | $", format(amount, '.2f'))
    amount += multi
    total += amount
    multi *= 2
print("\nCongratulations! you made a whopping $", format(total, '.2f'), "in", days, "days worth of work!")
