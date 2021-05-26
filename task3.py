from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!")
label1.pack()

# Create the message label and add it to the window using pack()
message_label1 = Label(root, textvariable=label1, wraplength=250)

#Create a PhotoImage()
neutral_image = PhotoImage(file="/images/python/neutral.png")

#Create a new Label using the PhotoImage and pack it into the GUI
image_label = Label(root, image=neutral_image)
image_label.pack()

# Create a second label with longer text and add it to the window using pack()

label2 = Label(root, text="This GUI app was created in 2021 by Marcel Wieringa")
label2.pack()

# Create a second message label and add it to the window using pack()
message_label2 = Label(root, textvariable=label2, wraplength=250)

# Run the main window loop
root.mainloop()
