# AirBnB_clone

AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interface.

This is part 1 of our AirBnb Clone project. The purpose of this project is to make a command interpreter that manages our AirBnb objects.


# Description of the commandline Interpreter
The Commandline Interpreter can be started by executing the command ./console.py. The console can create, destroy, and update objects. Type help within the console to get a list of command options and its function.

# Tabular Details of Folders, Files and Usage
| Folder | File | Description |
| ------ | ---- | ----------- |
| tests	|  | Contains test files for AirBnb Clone|
| models | base_model.py | Defines all common attributes/methods for other classes |
|  |  | To be updated soon |

## Using the console:

From project directory: `./console.py`

## Implemented console commands:
| command | functionality |
| --- | --- |
| quit | Same as default, quits interpreter. |
| EOF | (Ctrl + d) to quit |
| create | Creates a new object of the specified class, and returns its id. |
| show | Prints information about the specified object and its attributes. |
| destroy | Deletes object of specified id. |
| all | With no args, shows all objects, or all objects of a specified type. |
| update | Adds or updates the specified attribute for the specified object. |
