# this program determines whether the age given is for an infant, child, teenager or adult.
user_age = int(input("Please enter your age: "))

if user_age <= 1:
    print("This is the age of an infant.")
elif 1 < user_age < 13:
    print("This person is a child.")
elif 13 <= user_age < 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
