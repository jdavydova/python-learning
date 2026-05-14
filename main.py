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
