# this file demonstrates decision, structures, and conditions
def main():
    a = 7
    b = 4

    # exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater then A: {b > a}")
    print(f"A is equal to B: {a == b}")

    # comparison operators:
    # less than: <, greater than: >, less than or equal to: <=, greater than or equal to >=, equal to: ==

    # create a decision structure to determine if a and b are equal
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    # create a decision structure to print a letter grade based on a test score
    # A: 100 - 90, B: 89 - 80, C: 79 - 70, D: 69 - 60, F: less than 60
    print("Grade Decision: 1")
    test_score = 77

    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif ((test_score <= 89) and (test_score >= 80)):
        print(f"{test_score} --> B")
    elif ((test_score <= 79) and (test_score >= 70)):
        print(f"{test_score} --> C")
    elif ((test_score <= 69) and (test_score >= 60)):
        print(f"{test_score} --> D")
    elif ((test_score <= 59) and (test_score >= 0)):
        print(f"{test_score} --> F")
    else:
        print("Invalid test score")

    print("Grade Desicion: 2")
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score} --> A")
    elif (test_score >= 80):
        print(f"{test_score} --> B")
    elif (test_score >= 70):
        print(f"{test_score} --> C")
    elif (test_score >= 60):
        print(f"{test_score} --> D")
    elif (test_score >= 0):
        print(f"{test_score} --> F")
    else:
        print("Invalid test score")

    # create a deccision structure to determine the season: winter, spring, summer, fall
    # ask the user to enter the number of the month and based on the number, determine the season
    # winter - 12, 1, 2; spring - 3, 4, 5; summer - 6, 7, 8; fall - 9, 10, 11
    # output/print the season: "It is season"
    month_number = int(input("\nEnter a number: "))
    
    if ((month_number >= 3) and (month_number <= 5)):
        print("It is Spring")
    elif ((month_number >= 6) and (month_number <= 8)):
        print("It is Summer")
    elif ((month_number >= 9) and (month_number <= 11)):
        print("It is Fall")
    else:
        print("It is Winter")

main()
