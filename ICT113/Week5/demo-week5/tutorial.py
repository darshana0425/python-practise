"""
#1
a= 200
b= 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("b is not greater than a") """



""" 2. Generate a random number between 1 and 10 inclusive. Ask the user for an input. If the
input and the random number are the same, print “you guessed it right” else print “sorry,
better luck next time”.
"""
def main():
    import random
    random_no = random.randint(1,10)
    user_input = int(input("Enter a number between 1 and 10: "))
    if user_input == random_no:
        print("You guessed it right")
    else:
        print("Sorry, better luck next time. The number was", random_no)

# main()

"""Write a program that asks the user for number input to check and displays whether the
input number is odd or even. HINT: Use modulo operator
"""
def oddeven():
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 0:
        print(user_input, "is an even number.")
    else:
        print(user_input, "is an odd number.")

#oddeven()

""" 4.What is the output of the given program. Replace the for loop with a while loop but the
output should remain the same.
"""
def fruits():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break # exits the loop when x is "banana"
#fruits()


""" 5. What is the output of the given program. Replace the while loop with a for loop but the
output should remain the same."""

def numbers():
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue #skips the rest of the code in the loop for that iteration
        print(i)
#numbers()

"""6. Investigate the provided program (payroll-extended.py) by running it. Describe the
function of the program. Update the program to use function to print the payroll
summary report."""



"""7. Write a Python program that does the following:
Use a for loop to ask the user to enter the price of 5 items. For each item price:
a. If the price is greater than 0:
i. If the price is $50 or less, print “Affordable” and count it
ii. Otherwise, print “Too expensive”
b. If the price is invalid (0 or negative), print “Invalid price” and use continue
c. After all prices are entered, print the total number of affordable items.
"""
def check():
    affordable_count = 0
    for i in range(5):
        price = float(input("Enter the price of item {}: ".format(i + 1)))
        if price > 0:
            if price <= 50:
                print("Affordable")
                affordable_count += 1
            else:
                print("Too expensive")
        else:
            print("Invalid price")
            continue
    print("Total number of affordable items:", affordable_count)

#check()





"""
8. Write a Python program that:
a) Uses a while loop to repeatedly ask the user to enter a student’s mark
a. The loop should stop when the user enters -1 (use break)
b) For each valid mark (0–100):
a. Use if / elif / else to determine the grade:
i. 80 and above → HD
ii. 70–79 → D
iii. 60–69 → C
iv. 50–59 → P
v. Below 50 → F
b. Print the grade
c) If the mark is invalid (less than 0 or greater than 100), use continue to skip grading."""

def grade():
    while True:
        mark = int(input("Enter the student's mark (-1 to exit): "))
        if mark == -1:
            break
        elif 0 <= mark <= 100:
            if mark >= 80:
                print("Grade: HD")
            elif 70 <= mark < 80:
                print("Grade: D")
            elif 60 <= mark < 70:
                print("Grade: C")
            elif 50 <= mark < 60:
                print("Grade: P")
            else:
                print("Grade: F")
        else:
            print("Invalid mark. Please enter a value between 0 and 100.")
            continue

#grade()