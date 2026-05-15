import random

from pip._internal import operations

from helper import *

# EXERCISE 1: Working with Lists
my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

# Write a program that prints out all the elements of the list that are higher than or equal to 10.
for item in my_list:
    if item >= 10:
        print(item)

# Instead of printing the elements one by one, make a new list that has all the elements higher than or equal to 10 from this list in it and print out this new list.
new_list = []

for item in my_list:
    if item >= 10:
        new_list.append(item)

print(new_list)

# Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.

user_number = int(input("Enter a number: "))
new_list = []

for item in my_list:
    if item > user_number:
        new_list.append(item)

print(new_list)

# EXERCISE 2: Working with Dictionaries

employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Write a Python Script that:

# Updates the job to Software Engineer

employee["job"] = "Software Engineer"
print (employee["job"] )

# Removes the age key from the dictionary

# employee.__delitem__('age')
employee.pop("age")
print(employee)

# Loops through the dictionary and prints the key:value pairs one by one

for key, value in employee.items():
    print (f"{key}: {value}")

# Using the following 2 dictionaries:
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

# Write a Python Script that:

# Merges these two Python dictionaries into 1 new dictionary.

merg_dict = {**dict_one, **dict_two}
print(merg_dict)

# Sums up all the values in the new dictionary and prints it out

sums_of_dict = 0
for key, value in merg_dict.items():
    sums_of_dict += value

print(sums_of_dict)

# Prints the max and minimum values of the dictionary
merg_values = []
for key, value in merg_dict.items():
    merg_values.append(value)
print(merg_values)

merg_values.sort()
print(merg_values)

print(f"min value: {merg_values[0]}")
print(f"max value: {merg_values[-1]}")

# EXERCISE 3: Working with List of Dictionaries

# Using a list of 2 dictionaries:

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

# Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.

for employee in employees:
    print(f"name: {employee['name']}, job: {employee['job']}, city: {employee["address"]["city"]}")

# Prints the country of the second employee in the list by accessing it directly without the loop.

print (employees[1]["address"]["country"])

# EXERCISE 4: Working with Functions

# Write a function that accepts a list of dictionaries with employee age (see example list from Exercise 3) and prints out the name and age of the youngest employee.
get_youngest(employees)

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
calculate_case_letters("An Apple a Day keeps the Doctor away")

# Write a function that prints the even numbers from a provided list.
even_numbers(my_list)

# For cleaner code, declare these functions in its own helper Module and use them in the main.py file

# EXERCISE 5: Python Program 'Calculator'
# Write a simple calculator program that:

# takes user input of 2 numbers and operation to execute
# handles the following operations: plus, minus, multiply, divide
# does proper user validation and give feedback: only numbers allowed
# Keeps the Calculator program running until the user types “exit”
# Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did


def calculator(number_one, number_two, operation):
    if operation == "plus":
        return number_one + number_two
    if operation == "plus":
        print(number_one + number_two)
    elif operation == "minus":
        print(number_one - number_two)
    elif operation == "multiply":
        print(number_one * number_two)
    elif operation == "divide":
        print(number_one / number_two)

track_counter = 0

while True:
    number_one = input("Enter a first number: ")

    if number_one == "exit":
        print(f"Number of calculations is {track_counter}. Goodbye!")
        break

    number_two = input("Enter a second number: ")

    operation = input("Enter operation: plus, minus, multiply, divide:\n")
    if not number_one or not number_two:
        print("Input cannot be empty")
    elif not (number_one.isnumeric() and  number_two.isnumeric()):
        print ("The numbers are not valid")
    elif not (operation == "plus" or operation == "minus" or operation == "multiply" or operation == "divide"):
        print("The operations are not valid")
    else:
        calculator(int(number_one), int(number_two), operation)
        track_counter += 1

# EXERCISE 6: Python Program 'Guessing Game'
# Write a program that:
# runs until the user guesses a number (hint: while loop)
# generates a random number between 1 and 9 (including 1 and 9)
# asks the user to guess the number
# then prints a message to the user, whether they guessed too low, too high
# if the user guesses the number right, print out YOU WON! and exit the program
# Hint: Use the built-in random module to generate random numbers https://docs.python.org/3/library/random.html

random_number = random.randint(1, 9)
print(random_number)

while True:
    try:
        user_guesss_number = int(input("Enter a guess number between 1 and 9: "))
    except:
         print("The number is not valid")
         continue

    if user_guesss_number == random_number:
        print("YOU WON!")
        break
    elif user_guesss_number > random_number:
        print("Your guess is too high")
    elif user_guesss_number < random_number:
        print("Your guess is too low")
