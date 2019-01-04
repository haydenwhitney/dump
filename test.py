#Hayden Whitney
#1/19
#Test Taking Program

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "\nEnding program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the data file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answer = next_line(the_file)
        answers.append(answer)
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    the_file = open_file("test_data.txt", "r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print("\n", category)
        print(question)
        for i in range(4):
            print(answers[i])
        answer_input = input("ENTER THE LETTER OF THE CORRECT ANSWER: ").title()
        if answer_input == correct:
            print("Good job! +1 point")
            score += 1
        else:
            print("I'm not mad just disappointed. No points.")
        print(explanation)
        print("Score:", score, "\n")
    print("The final score is:", score)
    the_file.close()
    input("\n\nPress enter to exit.")
    

main()


