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
    a= 3
    b = 75
except (ValueError,ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"No error occurred. The result is: {result}")
    print("No error occurred. The result is: {}{}{}".format(result, a, b))


