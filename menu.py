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

def main():
    menu_items = get_menu_dictionary("file.txt")

    # print out menu items and prices
    for item, price in menu_items.items():
        print(f"{item}: ${price:.2f}")
    
    total_price = 0.0
    while True:
        # prompt user for menu items
        menu_input = input("\nItem:\n")

        # check if user input is in menu list
        # if yes, add price to total_price
        # if not, ignore and reprompt
        # check if user types end and end the loop if so
        
        if menu_input in menu_items:
            total_price += menu_items[menu_input]
        elif menu_input.lower() == "end":
            break
        else:
            continue
        
        # output total price
        print(f"Total: ${total_price:.2f}")

main()