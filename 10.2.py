import question


def main():
    question1 = question.Question("How many squares are on a Monopoly board?", "A. 60", "B. 20", "C. 80", "D. 40", "D")
    question2 = question.Question("What temperature is the same in Celsius and Fahrenheit?", "A. 100", "B. 40", "C. -40", "D. 0", "C")
    question3 = question.Question("What city does not have an official Disneyland?", "A. San Fransisco", "B. Hong Kong", "C. Tokyo", "D. Moscow", "D")
    question4 = question.Question("What animal first reached Earths orbit alive?", "A. Dog", "B. Cockroach", "C. Ape", "D. Tiger", "A")
    question5 = question.Question("What is the largest country by area that has only one time zone?", "A. Russia", "B. China", "C. Turkey", "D. Saudi Arabia", "B")
    question6 = question.Question("Which popular peer-to-peer network was shut down in October 2013?", "A. Megaupload", "B. The Pirate Bay", "C. isoHunt", "D. Lending Club", "A")
    question7 = question.Question("What is the color of the stars on the flag of the United States of America?", "A. Silver", "B. Gold", "C. Purple", "D. White", "D")
    question8 = question.Question("What did Alfred Nobel develop?", "A. TNT", "B. Dynamite", "C. C-4", "D. IED", "B")
    question9 = question.Question("How many times does a healthy human heart beat on average?", "A. 1,000", "B. 10,000", "C. 100,000", "D. 1,000,000", "C")
    question10 = question.Question("Which of these is not an insect?", "A. Tick", "B. Mosquito", "C. Flea", "D. Cricket", "A")

    p1_score = 0
    p2_score = 0
    player_turn = 0

    set_1 = [question1, question2, question3, question4, question5]
    set_2 = [question6, question7, question8, question9, question10]

    print("Ready, Player 1!: ")
    for queue in set_1:
        print("\n")
        print(queue.get_question())
        print(queue.get_a1())
        print(queue.get_a2())
        print(queue.get_a3())
        print(queue.get_a4())
        guess = input("Please enter the letter of your answer: ")
        if guess.upper() == queue.get_correct():
            print("Correct!")
            p1_score += 1
    print("Player 1's score is: " + str(p1_score) + " out of 5")

    print("Ready, Player 2!: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of your answer: ")
        if guess.upper() == query.get_correct():
            print("Correct!")
            p2_score += 1
    print("Player 2's score is: " + str(p2_score) + " out of 5")
    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p2_score > p1_score:
        print("Player 2 Wins!")
    else:
        print("Wow! It's a tie!!")

main()
