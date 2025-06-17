def main():
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
                continue
            answer = x / z

        # output the answer
        print(f"{expression} = {answer}")

        repeat_input = input("Would you like to do another calculation? (y/n): ")
        if repeat_input.lower() == "y":
            continue
        else:
            break

main()
