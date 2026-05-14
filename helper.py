def get_youngest (employees):
    yangest_age = employees[0]["age"]
    yangest_name = employees[0]["name"]
    for employee in employees:
        if yangest_age > employee["age"]:
            yangest_age = employee["age"]
            yangest_name = employee["name"]
    print (f"{yangest_name} is youngest: {yangest_age} years old!")

def calculate_case_letters(word):
    upper_letters = 0
    lower_letters = 0
    for letter in word:
        if letter.isupper():
            upper_letters += 1
        elif letter.islower():
            lower_letters += 1
    print(f"{upper_letters} upper and {lower_letters} lower")

def even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)
