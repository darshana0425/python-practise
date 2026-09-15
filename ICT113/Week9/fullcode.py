from tkinter import *
from tkinter import messagebox


# Function for the Submit button
def submit():
    name = nameEntry.get()

    # Get selected radio button
    gender = genderVar.get()

    # Get selected checkboxes
    subjects = []

    if pythonVar.get():
        subjects.append("Python")

    if htmlVar.get():
        subjects.append("HTML")

    if cssVar.get():
        subjects.append("CSS")

    # Get text from Text widget
    comment = textBox.get("1.0", END)

    # Display result
    result = "Name: " + name
    result += "\nGender: " + gender
    result += "\nSubjects: " + ", ".join(subjects)
    result += "\nComment: " + comment

    outputLabel.config(text=result)


# Function for clearing the form
def clear():
    nameEntry.delete(0, END)
    textBox.delete("1.0", END)

    genderVar.set("")

    pythonVar.set(0)
    htmlVar.set(0)
    cssVar.set(0)

    outputLabel.config(text="")


# Function for showing information
def show_info():
    messagebox.showinfo("Information", "This is a Tkinter GUI application.")


# Function for showing warning
def show_warning():
    messagebox.showwarning("Warning", "Please check your information.")


# Function for showing error
def show_error():
    messagebox.showerror("Error", "Something went wrong.")


# Function for asking a question
def ask_question():
    answer = messagebox.askyesno("Question", "Do you like Python?")

    if answer:
        outputLabel.config(text="You selected Yes")
    else:
        outputLabel.config(text="You selected No")


# Function to close the window
def close_window():
    root.destroy()


# -------------------------
# Main Window
# -------------------------

root = Tk()
root.title("Student Information")
root.geometry("600x700")


# -------------------------
# Label + Entry
# -------------------------

titleLabel = Label(
    root,
    text="Student Information",
    font=("Arial", 18)
)

titleLabel.grid(row=0, column=0, columnspan=3, pady=10)


nameLabel = Label(root, text="Enter your name:")

nameLabel.grid(row=1, column=0, padx=10, pady=10)

nameEntry = Entry(root, width=30)

nameEntry.grid(row=1, column=1, padx=10, pady=10)


# -------------------------
# Radiobutton
# -------------------------

genderLabel = Label(root, text="Select gender:")

genderLabel.grid(row=2, column=0, padx=10, pady=10)


genderVar = StringVar()

maleRadio = Radiobutton(
    root,
    text="Male",
    variable=genderVar,
    value="Male"
)

femaleRadio = Radiobutton(
    root,
    text="Female",
    variable=genderVar,
    value="Female"
)

otherRadio = Radiobutton(
    root,
    text="Other",
    variable=genderVar,
    value="Other"
)

maleRadio.grid(row=2, column=1)
femaleRadio.grid(row=2, column=2)
otherRadio.grid(row=3, column=1)


# -------------------------
# Checkbuttons
# -------------------------

subjectLabel = Label(root, text="Select subjects:")

subjectLabel.grid(row=4, column=0, padx=10, pady=10)


pythonVar = IntVar()
htmlVar = IntVar()
cssVar = IntVar()


pythonCheck = Checkbutton(
    root,
    text="Python",
    variable=pythonVar
)

htmlCheck = Checkbutton(
    root,
    text="HTML",
    variable=htmlVar
)

cssCheck = Checkbutton(
    root,
    text="CSS",
    variable=cssVar
)

pythonCheck.grid(row=4, column=1)
htmlCheck.grid(row=4, column=2)
cssCheck.grid(row=5, column=1)


# -------------------------
# Text Widget
# -------------------------

commentLabel = Label(
    root,
    text="Enter your comments:"
)

commentLabel.grid(row=6, column=0, padx=10, pady=10)


textBox = Text(
    root,
    width=40,
    height=6,
    font=("Arial", 12)
)

textBox.grid(row=6, column=1, columnspan=2, padx=10, pady=10)


# -------------------------
# Buttons
# -------------------------

submitButton = Button(
    root,
    text="Submit",
    command=submit
)

clearButton = Button(
    root,
    text="Clear",
    command=clear
)

infoButton = Button(
    root,
    text="Information",
    command=show_info
)

warningButton = Button(
    root,
    text="Warning",
    command=show_warning
)

errorButton = Button(
    root,
    text="Error",
    command=show_error
)

questionButton = Button(
    root,
    text="Ask Question",
    command=ask_question
)

closeButton = Button(
    root,
    text="Close",
    command=close_window
)


submitButton.grid(row=7, column=0, padx=5, pady=10)
clearButton.grid(row=7, column=1, padx=5, pady=10)
infoButton.grid(row=8, column=0, padx=5, pady=10)
warningButton.grid(row=8, column=1, padx=5, pady=10)
errorButton.grid(row=8, column=2, padx=5, pady=10)
questionButton.grid(row=9, column=0, padx=5, pady=10)
closeButton.grid(row=9, column=1, padx=5, pady=10)


# -------------------------
# Output Label
# -------------------------

outputLabel = Label(
    root,
    text="",
    bg="lightgray",
    width=60,
    height=8,
    anchor="nw",
    justify=LEFT
)

outputLabel.grid(
    row=10,
    column=0,
    columnspan=3,
    padx=10,
    pady=10
)


# -------------------------
# Start GUI
# -------------------------

root.mainloop()