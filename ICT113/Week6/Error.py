""" try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") """

try:
    mun = int(input("Enter a number: "))
    result = 10 / mun
    print("Result:", result)
except (ValueError,ZeroDivisionError) as e:
    print ("Error", e)

