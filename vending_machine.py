def main():
    # print vending machine
    print("Vending Machine")
    print("----------------")

    # initialize the amount due to 50
    amount_due = 50

    # use input function to get user input
    # use if statement to check if the number is in the list of coins that can be used
    # if not valid, restart the loop
    # if valid, reduce the amount of money entered from the amount due
    # stop loop when amount due is less than or equal to 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_entered = input("Insert Coin:\n")
        if coin_entered in ["1", "5", "10", "25"]:
            amount_due -= int(coin_entered)
        else:
            continue

    # change amount due to change owed and display the number
    change_owed = amount_due * -1
    print(f"Change Owed: {change_owed}")

main()