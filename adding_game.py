import random

"""
Function: get the difficulty level from the user
Input: none
Output: (int)level, (int)question_amount
"""
def get_level():
    while True:
        # prompt user for the level
        level = input("Enter level 1, 2, 3: ")

        # validate that input is either 1, 2, or 3 using an if statement
        # if not, output error and reprompt user
        if level not in ["1", "2", "3"]:
            print("Error: Invalid input\n")
            continue
        else:
            break

    while True:
        # ask user for the amount of questions between 3 and 10
        # validate that user input a number between 3 and 10
        # if not, output error and reprompt
        question_amount = input("Enter number of questions to ask: 3 to 10: ")
        if question_amount not in ["3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Error: Please enter an integer value between 3 and 10")
            continue
        else:
            break
    
    return int(level), int(question_amount)

"""
Function: generate math questions and check if user enters the correct answer
Input: (int)level, (int)question_amount
Output: (int)questions_correct
"""
def math_question_generator(level:int, question_amount:int):
    # check what level the user inputed and set the min and max for the random number
    if level == 1:
        min, max = 0, 9
    elif level == 2:
        min, max = 10, 99
    else:
        min, max = 100, 999
    random_generator = random.Random()

    questions_correct = 0
    questions_wrong = 0

    # use a for loop to go through the amount of questions the user wants
    # generate a random equation and their solution
    for question in range(question_amount):
        x = random_generator.randint(min, max)
        y = random_generator.randint(min, max)
        answer = x + y

        # use a while loop to ask user to enter the correct number
        # if user guesses wrong 3 times, move on to next question
        while questions_wrong != 3:
            # print out equation and get user's answer
            guess = input(f"\n{x} + {y} = ")
            if guess == str(answer):
                print("Correct!")
                questions_correct += 1
                break
            else:
                print("Incorrect!")
                questions_wrong += 1
                continue
        if questions_wrong == 3:
            print(f"Correct Answer: {x} + {y} = {answer}")
        questions_wrong = 0

    return questions_correct

def main():
    # use get_level function to get the difficulty level and amount of questions from the user
    level, question_amount = get_level()

    # use math_question_generator function to generate math questions using the values given and check if the user inputs the correct answer
    questions_correct = math_question_generator(level, question_amount)

    # divide the number of correct answers by the amount of questions
    percentage_correct = (questions_correct / question_amount) * 100

    # output the correct percentage
    print(f"\nYou got {questions_correct} out of {question_amount} correct: {percentage_correct:.2f}%")

main()