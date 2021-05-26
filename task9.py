from tkinter import *
from tkinter import ttk
import random

# Create an account class
class Comic:
  def __init__(self, name, balance, goal):
    self.name = name
    self.balance = balance
    self.goal = goal
    account_list.append(self)

# Create the money balance method
  def sell(self, amount):
    if amount > 0:
       self.balance += amount
       return True
    else:
        return False

# Create the money balance subtraction method
  def restock(self, amount):
      if amount > 0 and amount <= self.balance:
        self.balance -= amount
        return True
      else:
        return False

# Create the goal progress calculation method
  def get_progress(self):
      progress = (self.balance / self.goal) * 100
      return progress

# Create the function to read filr data
def get_data():
  account_file = open("accounts.txt", "r")
  line_list = account_file.readlines()

  for line in line_list:
    account_data = line.strip().split(",")
    Comic(*account_data)

  account_file.close()

# Create the names listing account function
def create_name_list():
  name_list = []
  for account in account_list:
    name_list.append(account.name)
  return name_list

# Create the balance updating function
def update_balance():
  total_balance = 0
  balance_string = ""
  account_file = open("accounts.txt", "w")

  # Create the accounts balance, progress, and goal to the label
  for account in account_list:
    progress = account.get_progress()
    balance_string += "{}:${:.2f} - {:.0f}% of ${} goal\n".format(account.name, account.balance, progress, account.goal)
    total_balance += account.balance
    account_file.write("{},{},{}\n".format(account.name,account.balance,account.goal))

  balance_string += "\nTotal balance: ${:.2f}".format(total_balance)
  account_details.set(balance_string)
  account_file.close()

# Create a sell function
def sell_comic(account):
  if account.sell(amount.get()):
    message = random.choice(restock_messages)
    message_text.set(message)
    action_feedback.set("Great! Total of ${:.2f} sold into {}").format(amount.get(), account.name)
  else:
    action_feedback.set("Please enter a proper number")

# Create a restock function
def restock_comic(account):
  if account.restock(amount.get()):
    message = random.choice(sell_messages)
    message_text.set(message)
    action_feedback.set("Great! Total of ${:.2f} restocked into {}").format(amount.get(), account.name)
  else:
     action_feedback.set("Please enter a correct number".format(account.name))

# Create a manage action function
def manage_action():
  try:
    for account in account_list:
      if chosen_account.get() == account.name:
        if chosen_action.get() == "Restock":
          sell_money(account)
        else:
          restock_money(account)

    # Update the GUI
    update_balance()
    amount.set("")

  # Add an exception for text input
  except ValueError:
    action_feedback.set("Please enter a valid number")
      

# Create lists
account_list = []
sell_messages = ["Great! We hope you enjoy your purchases!"]

restock_messages = ["We are sorry, but the comic books need to be restocked.", "Come back another day!"]

# Create class instances
get_data()
account_names = create_name_list()

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

1. Super Dude. Eight currently in stock.

2. Lizard Man. Twelve currently in stock.

3. Water Woman. Three currently in stock.""")
label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create and set the variable for the money 
account_details = StringVar()
account_details.set("Summary: $0 \nTotal sold: $0")

# Create the details label and have it packed into the GUI
details_label = ttk.Label(top_frame, textvariable=account_details)
details_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create an account combobox label
account_label = ttk.Label(root, text="Account: ")
account_label.grid(row=4, column=0, columnspan=2, padx=10, pady=3)

# Create a variable and option list for the a ccount Combobox
account_names = ["Super Dude", "Lizard Man", "Water Woman"]
chosen_account = StringVar()
chosen_account.set(account_names[0])

# Create a Combobox to select the account
account_box = ttk.Combobox(root, textvariable=chosen_account, state="readonly")
account_box['values'] = account_names
account_box.grid(row=5, column=0, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(root, text="Action")
action_label.grid(row=6, column=0)

# Create a variable and option list for the ation Combobox
action_list = ["Sell", "Restock"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create a Combobox to select the action
action_box = ttk.Combobox(root, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=7, column=0, padx=10, pady=3, sticky="WE")

# Create the amount field label and have it packed into the GUI
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=8, column=0, columnspan=2)

# Create a variable to store the amount in
amount = DoubleVar()
amount.set("")

# Create an entry for the amount
amount_entry = ttk.Entry(root, textvariable=amount)
amount_entry.grid(row=9, column=0, padx=10, pady=3, sticky="WE")

# Create the submit button
submit_button = ttk.Button(root, text="Submit", command=update_balance)
submit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Create a action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=11, column=0, columnspan=2)

# Run the main window loop
update_balance()
root.mainloop()
