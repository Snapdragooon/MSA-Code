def main():
    my_name = "sophie"

    # capitalize a string
    print(my_name.capitalize())

    # make a string uppercase
    print(my_name.upper())

    # make a string lowercase
    last_name = "SHEAHAN"
    print(f"{my_name.lower()} {last_name.lower()}")

    print("\nUsing startswith() method")
    # determine if a string starts with a set of characters
    print(my_name.startswith("s") or my_name.startswith("S"))

    if (not my_name.startswith("sop") and not my_name.startswith("Sop")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    print("\nUsing endswith() method")
    print(f"{my_name} ends with 'hie': {my_name.endswith("hie")}")

    print("\nUsing the find() method")
    # find the p in sophie
    search_letter = "x"
    print(f"The 'p' is at index {my_name.find("p")} in {my_name}")

    if (my_name.find(search_letter) == -1):
        print(f"There is no {search_letter} in {my_name}")
    else:
        print(f"The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")

    # loop through a string
    print("\nLoop through a string")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    # print the letters in a string along with the index position
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    
    # write code that counts the number of occurences of the word dog in the sentence
    # expected output: 3
    # search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    search_word = "dog"
    # use a while loop
    while True:
        # start at the beginning of the string
        # search for the first occurence of the word(dog) starting from index 0
        dog_index = sentence.find(search_word, start_index)
        # if we find a dog, add 1 to some variable of dogs we found
        # continue searching the string from the next index after the dog we found
        # update the start_index
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
            start_index = dog_index + 1
        # do this until we don't find any more dogs
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence")

    # how to use the split() method
    print("\nUsing the split() method")
    car_info = "Ferrari, F-50, 2021, 500000, 4.8"
    car_data = car_info.split(", ")
    print(car_data)
    # get individual pieces of data
    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price: ${price} - Engine: {engine_size}")

main()