from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!")
label1.pack()
# Create a second label with longer text and add it to the window using pack()

label2 = Label(root, text="This GUI app was created in 2021 by Marcel Wieringa")
label2.pack()
# Run the main window loop
root.mainloop()
