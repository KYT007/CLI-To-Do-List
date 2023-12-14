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

   

def run():  #Primary function that starts the program and allows the user to choose options
    # more options and functionalities TBA.
    while True:
        print("Please select an option: \n Main Menu \n. (A.) Make Note \n (B.) View Note \n (C.) Edit Note \n (D.) Delete Note")
        
        choice = pyip.inputChoice(['A', 'B', 'C', 'D'])
        if choice == "A":
            enter_item()
        elif choice == "B":
            read_item()
        elif choice == "C":
            edit_item()
        elif choice == "D":
            delete_item()

def enter_item():
    # For this section, we prompt the user for input asigned to variables,
    # these variables become the attributes of our class instance.
    # We then assign the instance to the variable "item" and append to storage.
    
    while True:
        title = pyip.inputStr("Please Enter a title: ")
        description = pyip.inputStr("Please Enter a description: ")
        due_date = pyip.inputStr("Please Enter a due date: ")
        item = ToDoItems(title, description, due_date)
        storage.append(item)
        print("****" + "Entry Saved!" + "*****")
        time.sleep(0.5)
        another_entry = pyip.inputChoice(["Yes", "No"], prompt="Do you want to add another item? (Yes/No): ")
        if another_entry == "No":
            break

    

def read_item():
    while True:
        for item in storage:
            print(f"{item.Title}, {item.Description}, {item.Due_Date}")
        if not storage:
            print("Looks like your storage is empty!")

        print("What would you like to do?\n(A.) Main Menu\n(B.) Edit")
        user_choice = pyip.inputChoice(["A", "B"])
        if user_choice == "A":
            break
        elif user_choice == "B":
            edit_item()

#The edit functionality allows the user to edit to-do items in storage. 
def edit_item():
    print(f"Please choose an item to edit: ")
    while True:
        if not storage:
            print("looks like there's no items here! ")
            return
        for index, item in enumerate(storage, start=1):
        # The code above shows us the storage list contents and numbers the items,
        #starting at 1.
       
            print(f"{index}, {item.Title}, {item.Description}, {item.Due_Date}") #here we allow the user to select the item they want to edit.
        index_slection = pyip.inputInt("Select item: ", min=1, max=len(storage))
        print(f"You've selected {index_slection}")
        #This code has the user enter the new information for the item they're editing
        new_title = pyip.inputStr("Please Enter a title: ")
        new_description = pyip.inputStr("Please Enter a description: ")
        new_due_date = pyip.inputStr("Please Enter a due date: ")
        edited_item = ToDoItems(new_title, new_description, new_due_date)
        storage[index_slection -1] = edited_item
        print(f"****" + "Item updated!" + "*****")
        time.sleep(0.3)
        break

def delete_item():
    print(f"*****" + "DELETE ITEMS" + "*****")
    while True:
        if not storage:
            print("looks like there's no items here! ")
            continue
        for index, item in enumerate(storage, start=1):
            print(f"{index}, {item.Title}, {item.Description}, {item.Due_Date}")

        selection = pyip.inputInt(min=1, max=len(storage), prompt= "Select index of item to be deleted, or '::' to quit: ")
        if selection:
            print("Are you sure? This action cannot be undone! y/n: ")
            choice = pyip.inputStr()
            if choice == "no":
                break
        
            
            
                
        
run()