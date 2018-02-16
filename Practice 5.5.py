import random


def main():
    for count in range(11):
        print("Question " + str(count+1) + ":")
        make_question()


def make_question():

    int_1 = random.randint(0, 1000)
    int_2 = random.randint(0, 1000)
    print("Solve the given equation\n")
    print(" " + str(int_1))
    print("+" + str(int_2))
    answer = int(input("Your answer: "))
    check_answer(answer, int_1, int_2)


def check_answer(answer, int_1, int_2):
    if answer == int(int_1) + int(int_2):
        print("Correct!")
    else:
        while answer != int_1 + int_2:
            print("Incorrect, try again")
            answer = int(input("Your answer: "))
main()
