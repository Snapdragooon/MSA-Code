# this file will demonstrate how for loops work

def main():
    # print integers between 0 and 10
    print("Output numbers between 0 and 10")
    for number in range(11):
        print(number)

    # print integers between 5 and 10
    print("\n\nOutput numbers between 5 and 10")
    for number in range(5, 11):
        print(number)
    
    # print even numbers between 0 and 10
    print("\n\nOutput even numbers between 0 and 10")
    for number in range(0, 11, 2):
        print(number)
    
    # print odd numbers between 0 and 10
    print("\n\nOutput odd numbers between 0 and 10")
    for number in range(1, 11, 2):
        print(number)

    # ask user for the start and stop values and print the numbers between start and stop
    # get thet start value from the user and convert to an integer
    # get the stop value from the user and convert to an integer
    # create a loop to run from start to stop
    start_value = int(input("Enter a start value: "))
    stop_value = int(input("Enter a stop value: "))

    print(f"\n\nOutput numbers from {start_value} to {stop_value}")
    for number in range(start_value, stop_value + 1):
        print(number)
    
    # use nested for loops to print multiplication tables from user input
    # user will provide start and stop values for the tables
    start_value = int(input("Enter a start value: "))
    stop_value = int(input("Enter a stop value: "))

    print(f"\n\nOutput multiplication tables from {start_value} to {stop_value}")
    for table in range(start_value, stop_value + 1):
        print(f"\nDisplaying the {table} multiplication table")
        for multiple in range(1, 13):
            product = table * multiple
            print(f"{table} x {multiple} = {product}")

main()