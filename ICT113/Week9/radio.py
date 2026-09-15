from tkinter import *

root = Tk()

# Checkbuttons
Label(root, text="Choose your subjects:").pack()

python = Checkbutton(root, text="Python")
html = Checkbutton(root, text="HTML")
css = Checkbutton(root, text="CSS")

python.pack()
html.pack()
css.pack()

# Radiobuttons
Label(root, text="Choose your year:").pack()

year = StringVar()

year1 = Radiobutton(root, text="Year 1", variable=year, value="Year 1")
year2 = Radiobutton(root, text="Year 2", variable=year, value="Year 2")
year3 = Radiobutton(root, text="Year 3", variable=year, value="Year 3")

year1.pack()
year2.pack()
year3.pack()

root.mainloop()