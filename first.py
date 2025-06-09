# print hello world
print("Hello World!")

# create a variable to store my first name
first_name = "Sophie"

# print "My name is Sophie"
print("My name is", first_name)

# create a variable to store my last name
last_name = "Sheahan"

# write a statement to display "My full name is Sophie Sheahan"
print("My full name is", first_name, last_name, sep="---")

# create variables to store your age, height, and weight, and assign them values
age = 16
height = 66
weight = 135.6

# print a sentence with age, height, and weight
print(f"My name is {first_name} {last_name}\nI am {age} years old, I am {height} inches tall, and I weigh {weight}lbs")

# get and print the data type for age, height, and weight
print(type(age))
print(type(height))
print(type(weight))

# write 3 print statements using string interpolation (fstring) to print descriptive sentences for the data types
# variable age is an int
print(f"Variable age is a {type(age)}")
print(f"Variable height is a {type(height)}")
print(f"Variable weight is a {type(weight)}")

number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"Total: {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")