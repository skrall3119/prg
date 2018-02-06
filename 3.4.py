package = (input("Which package did you purchase? "))
bill = 0

if package == "a" or package == "b" or package == "c":
    minutes = int(input("How many minutes have you used? "))
    if package == "a":
        if minutes > 450:
            bill = 39.99 + (minutes - 450) * 0.45
        else:
            bill = 39.99
    elif package == "b":
        if minutes > 900:
            bill = 59.99 + (minutes - 900) * 0.40
        else:
            bill = 59.99
    elif package == "c":
        bill = 69.99
    print("$", format(bill, '.2f'))
else:
    print("Please enter a valid package letter.")

