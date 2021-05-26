from tkinter import *
from tkinter import ttk

# Create the variable to store the account balance
savings_balance = 0

# Create the function to update the balance
def update_balance():
    global savings_balance
    deposit_amount = amount.get()
    savings_balance += deposit_amount
    total_balance = savings_balance
    account_details.set("Savings: ${:.2f}\nTotal Balance: ${:.2f}".format(savings_balance, total_balance))
    amount.set("")

# Create a window
root = Tk()
root.title("Comic book Store")

# Create a top frame
top_frame = ttk.LabelFrame(root, text="Comic books")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable for the window
message_text = StringVar()
message_text.set("My comic book store!")

# Create a message label and pack it
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create a label and add it to the window using pack()
label1 = Label(top_frame, text="This GUI app was created in 2021 by Marcel Wieringa")
label1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(top_frame, text="""This website was created to sell comics and has a vast variety in stock. They consist of:
1. Super Dude
2. Lizard Man
3. Water Woman """)
label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and set the variable for the money 
account_details = StringVar()
account_details.set("Savings: $0 \nTotal balance: $0")

# Create the details label and have it packed into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=3, column=0, columnspan=2)

# Create an account combobox label
account_label = ttk.Label(root, text="Account: ")
account_label.grid(row=4, column=0, columnspan=2, padx=10, pady=3)

# Create a variable and option list for the account Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(root, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=5, column=1, padx=10, pady=3)

# Create a label for the action Combobox
action_label = ttk.Label(root, text="Action")
action_label.grid(row=6, column=0)

# Create a variable and option list for the ation Combobox
action_list = ["Deposit", "Withdraw"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create a Combobox to select the action
action_box = ttk.Combobox(root, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=7, column=1, padx=10, pady=3)

# Create the amount field label and have it packed into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=7, column=0, columnspan=2)

# Create a variable to store the amount in
amount = DoubleVar()
amount.set("")

# Create an entry for the amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.grid(row=8, column=1, columnspan=2)

# Create the submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.grid(row=9, column=0, columnspan=2)

# Run the main window loop
root.mainloop()
