# Make a script that does addition and subtraction between two numbers/
value_1 = int(input("Enter first number: "))
operator = (input("Enter - or + : "))
value_2 = int(input("Enter second number: "))

if operator == "+":
    print("The sum is: " + str(value_1 + value_2))

elif operator == "-":
    print("The difference is: " + str(value_1 - value_2))

else: 
    print("Unknown operator")
