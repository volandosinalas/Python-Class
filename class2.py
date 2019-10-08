# If/Else Statements

# answer = input("Do you want to hear a joke? ")

# if answer.lower() == "yes":
#     print("I'm against picketing, but I don't know how to show it.")
#     # = Mitch Hedberg
# elif answer.lower() == "no": 
#     print("Fine.")
# else: 
#     print("I don't understand.")

# Lists in Python
the_count = [1, 2, 3, 4, 5]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 
                55, 
                "Anthony Wiener", 
                1/2, 
                ["Oh no", "A list inside of a list"]]

# Building lists from the ground up
people = []

people.append("Mattan")
people.append("Sarah")
people.append("Chris")
people.remove("Sarah")

print(people)

# Accessing elements of lists
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
third_animal = animals[2]
last_animal = animals[-1]

print("There are this many animals:", len(animals))
print("animals is a:", type(animals))

random_things[-1][0] # Pulls the "oh no" of the list within a list

# This for-loop goes through a list
for number in [1, 2, 5]:
    print(number)

for person in ["mattan", "alex", "sean"]:
    print(person.capitalize(), "likes cheese")

for number in the_count:
    print("This is count:", number)

for stock in stocks:
    print("Stock ticker:", stock)

for thing in random_things:
    print("Here's a random thing:", thing)

for _ in [1, 2, 3, 4, 5]:
    print("Hey")

for i in range(1, 11):
    print(i*i)