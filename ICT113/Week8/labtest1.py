"""3. Write a Python program that does the following:
a) Create a list of 5 subjects:
["Math", "English", "Science", "IT", "History"]
b) Ask the user to enter an index number.
c) Use a try / except block to:
o Print the subject at the given index
d) Handle the following errors:
o IndexError → if the index is out of range
o ValueError → if the input is not an integer
e) If no error occurs, print the selected subject."""

subjects=["Math","English","Science","IT","History"]
index = input("Enter an index number: ")
try:
    index = int(index)
    print("Selected subject:", subjects[index])
except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 4.")
except ValueError:
    print("Error: Please enter a valid integer.")       
