from tkinter import *

def displayName():
    nameEntered = myEntry.get()
    outputLabel.configure(text='Your name is ' + nameEntered)
    myEntry.delete(0, END)
    return

root = Tk()

myLabel = Label(root, text='Enter your name')

myEntry = Entry(root)
myEntry.insert(0, 'Name Please')

okButton = Button(root, text='OK', command=displayName)

outputLabel = Label(root, text='Wait for the result', height=2, bg='red', fg='white')

myLabel.grid(row=0, column=0)
myEntry.grid(row=1, column=0)
okButton.grid(row=2, column=0)
outputLabel.grid(row=3, column=0)

root.mainloop()