import time, pyinputplus as pyip
# Importing the necessary modules.

# A class defining our to do list items. Future iterations of this program may have more classes.
class ToDoItems:
    def __init__(self, Title, Description, Due_Date):
        self.Title = Title
        self.Description = Description
        self.Due_Date = Due_Date



storage = [] # for now, we will use this to store our to do list items. Later on,
# a database will be used.

def main_menu(): #Displays all menu options.
    print("Main Menu \n. (1.) Make Note \n (2.) Delete Note \n (3.) Edit Note")

def run():  #Primary function that starts the program and allows the user to choose options
    # more options and functionalities TBA.
    while True:
        main_menu()
        print("Please select an option: ")
        choice = input()
        if choice == "A":
            write_in()
        elif choice == "B":
            read_item()

def write_in():
    while True:
        tbe = input("Please Enter an item: ").title()
        storage.append(tbe)
        print("Entry Saved!")
        time.sleep(0.5)
        another_entry = pyip.inputChoice(["Yes", "No"], prompt="Do you want to add another item? (Yes/No): ")
        if another_entry == "No":
            break  # Exit the loop if the user chooses "No"
    





def read_item():
    pass