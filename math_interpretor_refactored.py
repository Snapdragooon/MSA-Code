"""
Function: to get valid expression inputs from the user
Input: none
Output: (int)x, (int)z, (string)y
"""
def get_valid_expression():
    while True:
        # prompt the user for an expression
        expression = input("Enter a math equation: ")
        # use the split() method to get the parts of the expression
        expression_list = expression.split(" ")
        # check the length of the list returned from .split
        if (len(expression_list) != 3): 
            # output Incorrect format message and reprompt(continue)
            print("Incorrect Format")
            continue
        
        try:
            # get X and Y and Z values from the list 
            # and check if X and Z are integers by converting to int()
            x = int(expression_list[0])
            z = int(expression_list[2])
        except:
            # output Error message and reprompt(continue)
            print("Please enter a number")
            continue

        # check that operator is +, -, *, /
        y = expression_list[1]
        if y not in ["+", "-", "*", "/"]:
            # output some error message
            # reprompt the user(continue)
            print("Please enter an operator (+, -, *, /)")
            continue

        break

    return x, y, z

"""
Function: to evaluate expression
Input: x(int), y(string), z(int)
Output: (int)answer
"""
def evaluate_expression(x:int, y:str, z:int):
    # determine the operation to carry out based on the value of the operator
    # use if/elif/else block to evaluate operator and carry out the appropriate operation
    if y == "+":
        answer = x + z
    elif y == "-":
        answer = x - z
    elif y == "*":
        answer = x * z
    else:
        if z == 0:
            print("Cannot divide by 0")
        else:
            answer = x / z
    return answer

def main():
    while True:
        # call tthe get_valid_expression_input function to get x, y, z
        int(x), str(y), int(z) = get_valid_expression

        # call evaluate_expression to get the answer for the expression
        answer = evaluate_expression(x, y, z)

        # print the answer
        print(f"{x} {y} {z} = {answer}")

        # ask user if they want to evaluate another expression
        # rerun the program if the user wants to continue, otherwise end the program
        repeat_input = input("Would you like to do another calculation? (y/n): ")
        if repeat_input.lower() == "y":
            continue
        else:
            break


main()