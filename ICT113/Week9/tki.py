from tkinter import *

root = Tk()

label1 = Label(root, text="00")
label2 = Label(root, text="01")
label3 = Label(root, text="02")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

root.mainloop()