#This program displays the day of the week given 1 = Monday, 2 = Tuesday, etc. based on user input

x = int(input("Enter a number for a day of the week. "))
if x == 1:
    print("Monday")
elif x == 2:
    print("Tuesday")
elif x == 3:
    print("Wednesday")
elif x == 4:
    print("Thursday")
elif x == 5:
    print("Friday")
elif x == 6:
    print("Saturday")
elif x == 7:
    print("Sunday")
else:
    print("Please pick a number between 1 and 7")
