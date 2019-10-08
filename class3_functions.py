def greet(): 
    return "Hey!"

def greet_by_name(name):
    return f"Hey {name}!"

def intro(person_1, person_2):
    return f"{person_1} I'd like to introduce you to {person_2}"

def divisible_by(number, divisor):
    return number % divisor == 0
#this returns true or false
#"refactoring" functions means making them shorter

def uppercase_and_reverse(text):
    return text.upper()[::-1]

def reverse(string):
    return string[::-1]

def is_pallindrome(string):
    return string.lower() == reverse(string).lower()