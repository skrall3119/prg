import random


def create_list():
    num_list = []
    for count in range(20):
        num_list.append(random.randint(1, 100))
    return sorted(num_list)


def get_input():
    try:
        user = int(input("Enter a number between 1 and 100: "))
    except ValueError:
        user = input('Please enter a valid number between 1 and 100: ')
    return int(user)


def clean_list(a_list, a_value):
    new_list = []
    for count in range(len(a_list)):
        if a_list[count] > a_value:
            new_list.append(a_list[count])
        count += 1
    print(new_list)
    if len(new_list) == 0:
        print("There are no numbers greater than the number you entered.")

my_list = create_list()
user_input = int(get_input())
clean_list(my_list, user_input)
