# function: determine name of the season based on the month
# input:(int)month_number
# output: (string)season_name
def get_season_name(month_number:int):
    if month_number in [3, 4, 5]:
        return "Spring"
    elif month_number in [6, 7, 8]:
        return "Summer"
    elif month_number in [9, 10, 11]:
        return "Fall"
    else:
        return "Winter"

# fuction: get the month number from the user
# input: none
# output: (int)month_number
def get_month_number():
    # validate the input is 1 - 12
    # # reprompt user if input is not valid
    while True:
        try:
            number = int(input("Enter month number: "))
            if (number <= 0) or (number > 12):
                print("Please enter a number between 1 and 12")
                continue
            else:
                break
        except:
            print("Please enter a number") 
    return number  

def main():
    while True:
        # call the get_month_number function to prompt and get the month number from the user
        month_number = get_month_number()

        # call the get_season_name function to get the name of the season
        season_name = get_season_name(month_number)

        # print the output
        print(f"It is {season_name}")

        # ask the user if they want to run the program again
        # if y or Y, rerun the program, otherwise end the program
        rerun_input = input("Would you like to run program again? (y/n): ")
        if rerun_input.lower() == "y":
            continue
        else:
            break

main()