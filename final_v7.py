####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random

### LISTS ###
comic_list = []


##################  CLASS CODE  ######################
# Create the  class
class Comic:
  def __init__(self, name, balance):
    self.name = name
    self.balance = int(balance)

    comic_list.append(self)

  # REstock method adds money to balance
  def restock(self, amount):
    if amount > 0:
      self.balance += int(amount)
      return True
    else:
      return False

  # Sell method subtracts money from balance
  def sell(self, amount):
    if amount > 0 and amount <= self.balance:
      self.balance -= int(amount)
      return True
    else:
      return False

##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file
def get_data():
  comic_file = open("accounts.txt", "r")
  line_list = comic_file.readlines()
  
  for line in line_list:
    comic_data = line.strip().split(",")
    Comic(*comic_data)

  comic_file.close()
get_data()

# Create a function to get comic names list
def create_name_list():
  name_list = []
  for comic in comic_list:
    name_list.append(comic.name)
  return name_list

# Create a function that will update the balance.
def update_balance():
  total_balance = 0
  balance_string = ""
  comic_file = open("accounts.txt", "w")

  # Append each accounts balance, progress and goal to the label
  for comic in comic_list:

    balance_string += "{}: {} in stock\n".format(comic.name, comic.balance)
    total_balance += comic.balance
    comic_file.write("{},{}\n".format(comic.name,comic.balance))

  balance_string += "\nTotal balance: ${}".format(total_balance)
  comic_details.set(balance_string)
  comic_file.close
  
# Create the sell comic function
def sell_comic(comic):
  if comic.sell(amount.get()):
    message = random.choice(restock_messages)
    message_text.set(message)
    action_feedback.set("Great! Total of {} sold from {}".format(amount.get(), comic.name))
 
  else:
    action_feedback.set("Please enter a proper number")

# Create the restock function
def restock_book(comic):
  if comic.restock(amount.get()):
    message = random.choice(sell_messages)
    message_text.set(message)
    action_feedback.set("Great! Total of {:.2f} restocked into {}".format(amount.get(), comic.name))
   
  else:
    action_feedback.set("Please enter a correct number".format(comic.name))

# Create the manage action function
def manage_action():
  try:
    for comic in comic_list:
      if chosen_comic.get() == comic.name:
        if chosen_action.get() == "Restock":
          restock_book(comic)
        else:
          sell_comic(comic)

    # Update the GUI
    update_balance()
    amount.set("")

  # Add an exception for text input
  except ValueError:
    action_feedback.set("Please enter a valid number")


# Set up Lists
sell_messages = ["Well done, keep those deposits coming!", "You're making good progress!","Awesome! It will feel great when you reach your goal"]
restock_messages = ["Think about where else you might be able to save some money this week","You're doing well, but try to keep that spending under control","Tomorrow is another day for saving!"]


# Create instances of the class
#super_dude = Comic("Super Dude", 12)
#lizard_man = Comic("Lizard Man", 8)
#water_women = Comic("Water Women", 3)
comic_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Comic book store")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Comic books")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("My comic book store!")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="book.png")
happy_image = PhotoImage(file="smiley.jpg")
sad_image = PhotoImage(file="smiley.jpg")

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create and set the comic details variable
comic_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=comic_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the comic combobox
comic_label = ttk.Label(bottom_frame, text="comics: ")
comic_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the comic Combobox
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the comic
comic_box = ttk.Combobox(bottom_frame, textvariable=chosen_comic, state="readonly")
comic_box['values'] = comic_names
comic_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action Combobox
action_label = ttk.Label(bottom_frame, text="Action:")
action_label.grid(row=4, column=0) 

# Set up a variable and option list for the action Combobox
action_list = ["Sell", "Restock"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_balance()
root.mainloop()
