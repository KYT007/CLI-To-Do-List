#A Simple C.R.U.D. Program Using Pyinputplus for Input Validation

The program contained in this repository will be a C.R.U.D. type app I will be creating and continously adding to as I continue to learn more about the python programming language
and software engineering. This application will start out simple and be updated as I expand my knowledebase.
As I learn the usage of databases, how to implement GUIs and similar concepts, this program will grow and change.


Update for SimpleCRUD.py 11/19/2023

#Fixed Issues.

Detected and fixed many errors with the base framework of the protoype program.
Input validations using pyip were not implemented where they should have been. 
Items were not being properly appended to storage as class objects as they were inteded to be.

read_item() function updated for errors, title() attribute was unneeded. 

12/4/2023, 12/7/2023.
#Features added. 
Edit item function was added in. Read and write_in functions updated to suit this development.
Delete_item() functionality stage set.

##Fixed multiple issues.
Fixed multiple positional arguments issues.
".Title" in line 77, letter T was not capitalized, throwing an error. 
Replaced some variable names with more sensible (and less nonsensical) ones.

##Bad Design in Flow Control error discovered from exiting edit function.
The flow control of this program is flawed from the maker's perspective. Current possibilities for refactoring being considered and will be implemented by the next update.

#####Fixed spelling errors in the readme.

Those were embarassing. 

12/8/2023
#Fixed flow control issues that made the program not make sense.

Program organized to always return to main event loop after user is done using write, read, or edit functions.
The issue previouisly was bugging me. No pun intended.

##Added functionality.

Delete functionality added. Adding proper date detection functionality with pyip is incoming.

12/13/2023
#Added functionality, removed unnecessary items, experimenting 

Delete functionality under construction. Got rid of unnecessary print statements. Fixed loop issue with delete function. Data-Persistent (usable) version of program featuring use of SQLite TBA.

12/20/2023
#Added Functionality.
Added delete functionality in its entirety. Functionality to ensure valid dates added via pyinputplus added.
More flow control isues addressed. Main change main menu loop function to incorporate the use of "inputMenu()" from pyip rather than "inputChoice()". Unnecessary print statements removed. Future versions will use an alternative method to print statements.
SQLite Database functionality to make this app fully functional and usable as a command line tool currently in development process in a separate directory.
