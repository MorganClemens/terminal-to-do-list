# Contains app logic for user interaction within the terminal interface
import models

class App():
    '''Will utilize ToDoList class to define user interactions.'''

    def __init__(self):
        self.toDoList = models.ToDoList() # create new to do list object
        self.working_item = "" # stores the current working item
        self.error_codes = [] # stores any error codes

    def read_input(self):
        '''Prompts and parses user input. Returns int corresponding to command.'''
        user_input = input("Enter command: ")
        # Parse user input
        user_input_split = user_input.split()
        user_command = user_input_split[0]

        for word in user_input_split[1:]:
            self.working_item += (word + " ") # assemble and store item as working item

        # Handle invalid input
        valid_commands = ["add", "finish", "remove", "quit"]
        if user_command.lower() not in valid_commands:
            # invalid if too many arguments or unrecognized command
            self.error_codes.append("Invalid command.")

        # Read command

        match user_command:
            case "add":
                return 0
            case "finish":
                return 1
            case "remove":
                return 2
            case "quit":
                return 3
            case _:
                return -1
            
    def execute_command(self, command_index):
        '''Reads the command index and executes the corresponding command.'''
        match command_index:
            case 0:
                self.toDoList.add_item(self.working_item) # add current working item to the to-do list
            case 1:
                self.toDoList.finish_item(self.working_item) # finish current working item from to-do list
            case 2:
                self.toDoList.remove_item(self.working_item) # delete current working item from to-do list
            case 3:
                print("Quitting...")
                quit() # quits the session - will need to verify this works later
            case -1:
                self.error_codes.append("Command error.") # Append error code

        self.working_item = "" # Clear the working item