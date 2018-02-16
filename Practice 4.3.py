months = 0
totalRain = 0
years = int(input("please enter the number of years: "))

for currentYear in range(1, years + 1):
    for currentMonth in range(1, 13):
        monthlyRain = float(input("Please type the inches of " + "rainfall for month "+format(currentMonth, "d") + " year "+ format(currentYear,"d")+ ":"))
        totalRain += monthlyRain
        months += 1
averageRainfall = totalRain / months

print("\nNumber of months:", format(months,"d"), "Total inches of rainfall:", format(totalRain, ".2f"), "average rainfall:", format(averageRainfall, ".2f"))
