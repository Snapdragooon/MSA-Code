"""
Function: to load menu item and price into a dictionary
Input: (string)file_path
Output: (dictionary)menu
"""
def get_menu_dictionary(file_name:str) -> dict:
    # open file.txt: create a file handler in read mode
    data_file = open(file_name, "r")

    # create an empty dictionary to store item: price entries
    menu_items = {}

    # use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # split the data at the comma
        item_name_and_price = line_of_data.split(",")
        
        # get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        # create an entry in the dictionary for the item and price 
        menu_items[item_name] = item_price

    data_file.close()
    return menu_items

def display_cart(cart:dict, menu_items:dict) -> None:
    print("\nCart:\n-----")
    total = 0
    # loop through the cart to print the output
    for item, quantity in cart.items():
        total += (menu_items[item] * quantity)
        print(f"{quantity} {item} @ {menu_items[item]:.2f}: {(menu_items[item] * quantity):.2f}")
    print(f"\nTotal: {total:.2f}")

"""
Function: to write items from cart to a receipt
Input: (dict)cart
Output: none
"""
def print_receipt(cart:dict, menu_items:dict) -> None:
    with open("receipt.txt", "w") as receipt_file:
        total = 0
        # loop through the cart to print the output
        for item, quantity in cart.items():
            total += (menu_items[item] * quantity)
            receipt_file.write(f"{quantity} {item} @ {menu_items[item]:.2f}: {(menu_items[item] * quantity):.2f}\n")
        receipt_file.write(f"Total: {total:.2f}\n")

def main():
    menu_items = get_menu_dictionary("file.txt")

    # print out menu items and prices
    for item, price in menu_items.items():
        print(f"{item}: ${price:.2f}")

    # create a cart dictionary
    item_cart = {}

    while True:
        # prompt user for menu items
        menu_input = input("\nItem:\n")

        # check if user types end and break loop if so
        if menu_input.lower() == "end":
            # print the receipt with items from the cart
            print_receipt(item_cart, menu_items)
            break

        # check if user input is in menu dictionary
        # if not, ignore and reprompt
        if menu_input not in menu_items:
            print(f"ERROR: {menu_input} not on the menu")
            continue

        # prompt user for quantity
        try:
            quantity = int(input("Quantity:\n"))
        except:
            print("\nERROR: enter number for quantity")
            continue

        # add item to cart, if item is already in cart, add quantity
        # if not in cart, add item and quantity to cart
        if menu_input not in item_cart:
            # create a new entry in the item_cart dictionary
            item_cart[menu_input] = quantity
        else:
            # add quantity to existing item in cart
            item_cart[menu_input] += quantity

        # output total price and items ordered
        """
        2 Taco @ 3.00: 6.00
        3 Bowl @ 8.50: 25.50

        Total: 31.50
        """
        display_cart(item_cart, menu_items)

main()
