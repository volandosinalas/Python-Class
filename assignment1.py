# Intro to Programming Using Python - Assignment #1
# Completed by:

# 1. Print out the following text: 
# You've reached [your name]. 
# I'm not available right now, so leave a message and I'll call you back.

print("You've reached Nicky.") 
print("I'm not available right now, so leave a message and I'll call you back.")

# 2. Create five variables for your first name, last name, shoe size, height, and age. 
# And then print them out on one line.

first_name = "Nicky"
last_name = "Corbett"
shoe_size = 6
height = 5
age = 34

print(first_name, last_name, "wears a size", shoe_size, "shoe, is", height, "feet tall, and is", age, "years old.")

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.

total = 10.58 + (10.58 * 0.22) 

print(total)
 
# 4. Convert 158.8 into an integer. 
# Convert 75 into a float. 
# Convert "244.9" into a float and then an integer.
int(158.8)
#Converts to 158

float(75)
#Converts to 75.0

int(float(244.9))
#converts to 244

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
# 
#                               sing


# \t means tab and \n means new line
print("-in the woods \n \t which \n \t \t stutter \n \t \t \t and \n \n \t \t \t \t sing")

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: 
# Mattan, your total is $12.91 
# (remember to round the total to the nearest cent)
print(f"{first_name}, your total is ${round(total, 2)}")

# 7. Use input() to ask a user for the city they live in, and then print it back to them.
answer = input("What city do you live in?")
print(answer)

# 8. Build a future value calculator by using input() to get values from the user. 
# (Make sure you convert them into integers or floats before doing any math on them.) 
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

present_value = float(input("How much money do you have in your high-yield savings account?"))
rate_of_return = float(input("What is the monthly interest rate on the account?"))
period = int(input("How many months will you keep that money in the account?"))

future_value = present_value * (1 + rate_of_return) ** period
print(future_value)