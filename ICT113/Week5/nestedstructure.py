def main():
    count = 0
    # Ask useer for the input 10 times
    for counter in range(10):
        number = int(input("Enter a number: "))
        # Check is the input is greater than 10
        if (number> 10):
            count += 1

    print("You entered", count, "numbers greater than 10")

main()