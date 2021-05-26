from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create and set the message text variable for the window
message_text = StringVar()
message_text.set("My GUI App!")

# Create a label and add it to the window using pack()
label1 = Label(root, text="This GUI app was created in 2021 by Marcel Wieringa")
label1.pack()

# Create the message label and add it to the window using pack()
message_label1 = Label(root, textvariable=label1, wraplength=250)


# Create a second label with longer text and add it to the window using pack()

label2 = Label(root, text="""This website was created to sell comics and has a vast variety in stock. They consist of:
1. Super Dude
2. Lizard Man
3. Water Woman """)
label2.pack()

# Create a second message label and add it to the window using pack()
message_label2 = Label(root, textvariable=label2, wraplength=250)

# Create and set the variable for the money 
account_details = StringVar()
account_details.set("Savings: $460 - 25% of $1840 goal\nTotal balance: $460")

# Create the details label and have it packed into the GUI
details_label = Label(root, textvariable=account_details)
details_label.pack()

# Create the amount field label and have it packed into the GUI
amount_label = Label(root, text="Amount:")
amount_label.pack()

#Create a variable to store the amount in
amount = DoubleVar()
amount.set("")

#Create an entry for the amount
amount_entry = Entry(root, textvariable=amount)
amount_entry.pack()

# Run the main window loop
root.mainloop()
