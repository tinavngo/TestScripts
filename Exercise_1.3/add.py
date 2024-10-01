# Add inputs
a = input("Enter a number:")
b = input ("Enter another number to be added to the first: ")
# Convert the strings to numeric data types
a = int(a)
b = int(b)
print("The sum of these numbers is: ", a + b)
# Shorter, rewritten code
a = int(input("Enter a number: "))
b = int(input("Enter another number to be added to the first: "))
print("The sum of these numbers is:" + str(a + b))

# Number operators // two different outputs either true or false
age = int(input("Enter your age:"))
print("Age between 18 and 35" + str(18 < age < 35))
