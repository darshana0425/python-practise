"""2. Write a Python program that:
a) Asks the user to enter two numbers.
b) Uses a try / except block to:
o Convert the inputs to integers
o Divide the first number by the second number
c) Handle the following errors:
o ValueError → if the user enters a non-numeric value
o ZeroDivisionError → if the second number is zero
Example:
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero """

a = input("Enter first number: ")
b = input("Enter second number: ")  
try:
    a = int(a)
    b = int(b)
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")