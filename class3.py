# You can use dictionaries to store sets of key value pairs
# With dictionaries, order doesn't matter, unlike with lists. 
# You have to use a key. Keys are always strings.
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

list_of_states = ["New York", "Pennsylvania", "California"]
print(list_of_states[0])

# This is how you add something to a dictionary
# You can also Google for Python dictionaries of common lists and copy and paste it in
states["FL"] = "Florida"
print(states)

#Dictionaries Challenge
user = {'name': 'Nicky', 
        'height': 60, 
        'shoe size': 6,
        'hair': 'brown', 
        'favorite movies': ['Beetlejuice', 
                            'The Wedding Singer',
                            'Lord of the Rings']}

print(f"{user['name']}, has {user['hair']}, hair and the following favorite movies: {user['favorite movies']}")

#Defining Functions (name is the argument)

import class3_functions

print(class3_functions.greet())


print(class3_functions.greet_by_name("Mattan"))


print(class3_functions.intro("Mattan", "Angela"))

from class3_functions import divisible_by, uppercase_and_reverse, reverse, is_pallindrome

print(divisible_by(15, 3))
print(divisible_by(20, 3))

#Function Challenge 2


print(uppercase_and_reverse("banana"))
# [::-1] makes a string read in the reverse

#Function Challenge 3


print(reverse("hello")) 


print(is_pallindrome("madam"))
print(is_pallindrome("hello"))
print(is_pallindrome("Madam"))

