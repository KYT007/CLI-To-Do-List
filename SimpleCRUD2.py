import time, pyinputplus as pyip, sys, sqlite3
# Importing the necessary modules, including SQLite3 for database functionality.

###TO BE ADDED###
#Code that allows user to exit functions at the beginning of function, before performing an operation.

conn = sqlite3.connect('storage.db')
crudcursor = conn.cursor()

crudcursor.execute('''
    CREATE TABLE IF NOT EXISTS to_do_items (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        Due_Date TEXT
                   
    )
''')


# A class defining our to do list items. Future iterations of this program may have more classes.
class ToDoItems:
    def __init__(self, Title, Description, Due_Date):
        self.Title = Title
        self.Description = Description
        self.Due_Date = Due_Date





def run():  #Primary function that starts the program and allows the user to choose options
    # more options and functionalities TBA.
    while True:
        print("Please select an option: \n Main Menu \n. (A.) Make Note \n (B.) View Note \n (C.) Edit Note \n (D.) Delete Note \
\nEnter :: from main menu to quit: ")      
        
        choice = pyip.inputChoice(['A', 'B', 'C', 'D', '::'])
        if choice == "A":
            enter_item()
        elif choice == "B":
            read_item()
        elif choice == "C":
            edit_item()
        elif choice == "D":
            delete_item()
        elif choice == "::":
            print('Goodbye!')
            conn.close()
            sys.exit()

def enter_item():
    # For this section, we prompt the user for input asigned to variables,
    # these variables become the attributes of our class instance.
    # We then assign the instance to the variable "item" and append to storage.
    
    while True:
        title = pyip.inputStr("Please Enter a title: ")
        description = pyip.inputStr("Please Enter a description: ")
        due_date = pyip.inputStr("Please Enter a due date: ")
        


        crudcursor.execute('''
            INSERT INTO to_do_items (Title, Description, Due_date)
            VALUES (?, ?, ?)
        ''', (title, description, due_date))

        # Commit the changes to the database
        conn.commit()

        print("****" + "Entry Saved!" + "*****")
        time.sleep(0.5)
        another_entry = pyip.inputChoice(["Yes", "No"], prompt="Do you want to add another item? (Yes/No): ")
        if another_entry == "No":
            break

    

def read_item():
    while True:
       # Execute a SELECT query to retrieve data from the database
        crudcursor.execute('SELECT * FROM to_do_items')

        # Fetch all rows from the result set
        rows = crudcursor.fetchall()

        # Check if there are any rows to display
        if not rows:
            print("No items found.")
            break  # Exit the loop if there are no items

        # Display the items
        for row in rows:
            item_id, title, description, due_date = row
            print(f"Item ID: {item_id}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Due Date: {due_date}")
            

        print("What would you like to do?\n(A.) Main Menu\n(B.) Edit")
        user_choice = pyip.inputChoice(["A", "B"])
        if user_choice == "A":
            break
        elif user_choice == "B":
            edit_item()

#The edit functionality allows the user to edit to-do items in storage. 
def edit_item():
    while True:
        # Display existing entries to the user
        crudcursor.execute('SELECT * FROM to_do_items')
        rows = crudcursor.fetchall()

        if not rows:
            print("No items found.")
            return

        print("Existing items:")
        for row in rows:
            item_id, title, description, due_date = row
            print(f"Item ID: {item_id}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Due Date: {due_date}")
            

        # Prompt the user to select an item to edit
        try:
            item_id_to_edit = pyip.inputInt("Enter the Item ID you want to edit: ")

            # Check if the selected item_id exists
            crudcursor.execute('SELECT * FROM to_do_items WHERE id = ?', (item_id_to_edit,))
            existing_item = crudcursor.fetchone()

            if not existing_item:
                print(f"Item with ID {item_id_to_edit} not found.")
                continue

            # Prompt the user for updated values
            new_title = pyip.inputStr("Enter the new title: ")
            new_description = pyip.inputStr("Enter the new description: ")
            new_due_date = pyip.inputStr("Enter the new due date: ")

            # Update the database with the new values
            crudcursor.execute('''
                UPDATE to_do_items
                SET Title = ?, Description = ?, Due_date = ?
                WHERE id = ?
            ''', (new_title, new_description, new_due_date, item_id_to_edit))

            conn.commit()
            print(f"Item with ID {item_id_to_edit} updated successfully.")
        except ValueError:
            print("Invalid item ID! Please enter a valid item ID: ")
            break
        another_edit = pyip.inputChoice(["Yes", "No"], prompt="Do you want to edit another item? (Yes/No): ")
        if another_edit == "No":
            run()
            
#The delete function, allows user to delete items in storage.
            
def delete_item():
    while True:
        # Display existing entries to the user
        crudcursor.execute('SELECT * FROM to_do_items')
        rows = crudcursor.fetchall()

        if not rows:
            print("No items found.")
            return

        print("Existing items:")
        for row in rows:
            item_id, title, description, due_date = row
            print(f"Item ID: {item_id}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Due Date: {due_date}")
            

        # Prompt the user to select an item to edit
        try:
            item_id_to_delete = pyip.inputInt("Enter the Item ID you want to delete: ")

            # Check if the selected item_id exists
            crudcursor.execute('SELECT * FROM to_do_items WHERE id = ?', (item_id_to_delete,))
            existing_item = crudcursor.fetchone()

            if not existing_item:
                print(f"Item with ID {item_id_to_delete} not found.")
                continue
            answer = pyip.inputYesNo("Are you sure you want to delete this item? This can't be undone: ")
            if answer == 'yes':
                # Update the database with the new values and notify the user.
                crudcursor.execute('DELETE FROM to_do_items WHERE id = ?', (item_id_to_delete))
                conn.commit()
            elif answer == 'no':
                continue
            print(f"Item with ID {item_id_to_delete} updated successfully.")
        except ValueError:
            print("Invalid item ID! Please enter a valid item ID: ")
            break
        #Ask if the user would like to delete another item.
        another_delete = pyip.inputChoice(["Yes", "No"], prompt="Do you want to edit another item? (Yes/No): ")
        if another_delete == "No":
            run()
                

run()