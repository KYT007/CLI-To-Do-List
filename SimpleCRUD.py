import time, pyinputplus as pyip
# Importing the necessary modules.

# A class defining our to do list items. Future iterations of this program may have more classes.
class ToDoItems:
    def __init__(self, Title, Description, Due_Date):
        self.Title = Title
        self.Description = Description
        self.Due_Date = Due_Date



storage = [] # for now, we will use this to store our to do list items. Later on,
# a database will be used. Its important to note this program is only a prototype.

def main_menu(): #Displays all menu options.
    print("Main Menu \n. (A.) Make Note \n (B.) Delete Note \n (C.) Edit Note")

def run():  #Primary function that starts the program and allows the user to choose options
    # more options and functionalities TBA.
    while True:
        main_menu()
        print("Please select an option: ")
        choice = pyip.inputChoice(['A', 'B', 'C'])
        if choice == "A":
            write_in()
        elif choice == "B":
            read_item()

def write_in():
    # For this section, we prompt the user for input asigned to variables,
    # these variables become the attributes of our class instance.
    # We then assign the instance to the variable "item" and append to storage.
    
    while True:
        title = pyip.inputStr("Please Enter a title: ")
        description = pyip.inputStr("Please Enter a description: ")
        due_date = pyip.inputStr("Please Enter a due date: ")
        item = ToDoItems(title, description, due_date)
        storage.append(item)
        print("Entry Saved!")
        time.sleep(0.5)
        another_entry = pyip.inputChoice(["Yes", "No"], prompt="Do you want to add another item? (Yes/No): ")
        if another_entry == "No":
            break

    

def read_item():
    while True:
        for item in storage:
            print("\nTitle:", item.Title)
            print("Description:", item.Description)
            print("Due Date:", item.Due_Date +"\n")
        if not storage:
            print("Looks like your storage is empty!")

        print("What would you like to do?\n(A.) Main Menu\n(B.) Edit")
        RRchoice = pyip.inputChoice(["A", "B"])
        if RRchoice == "A":
            break 
def edit_item():
    pass

run()