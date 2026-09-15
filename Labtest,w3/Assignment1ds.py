# Name : Darshana Shrestha
# student no: 989212


def main():
    # Input name of the fruit
    fruit_name = input("Enter the name of the fruit ")
    # Input quantity of the fruit
    fruit_qty = int(input("Enter the quantity of the fruit "))
    # Importing math library
    import math
    price = int(math.cbrt(989212))
    # Calculate total price of fruit
    total_price = fruit_qty * price
    print(" Price of ",fruit_qty," ",fruit_name, "is $", total_price)

main()



