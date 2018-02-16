# takes a list as a parameter and calculates the average of the list.
def calc_average(score_list):
    total = 0
    for counter in range(len(score_list)):
        total += score_list[counter]
    average = total / 5
    return average


# Compares the parameter with the given conditions and returns the grade based on the conditions
def determine_grade(percentage):
    if percentage < 60:
        print("F")
    elif 60 <= percentage <= 69:
        print("D")
    elif 70 <= percentage <= 79:
        print("C")
    elif 80 <= percentage <= 89:
        print("B")
    elif 90 <= percentage <= 100:
        print("A")


# initializes a list, takes 5 inputs from user, stores them in a list, and finds the grade based on the scores.
scores = []
for count in range(5):
    scores.append(int(input("enter 5 test scores: ")))
    count += 1
grade_percentage = calc_average(scores)
print(grade_percentage)
determine_grade(grade_percentage)
