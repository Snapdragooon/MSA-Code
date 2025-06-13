# function to add 3 numbers
# input: (int)number_1, (int)number_2, (int)number_3
# output: (int)total
def add_number(number_1, number_2, number_3):
    total = number_1 + number_2 + number_3
    c = 18
    return total

def main():
    a = 5
    b = 4
    c = 3

    # call the add_numbers function and assign the returned value to answer
    answer = add_number(a, b, c)
    print(f"{a} + {b} + {c} = {answer}")
    print(f"Variable c = {c}")

main()