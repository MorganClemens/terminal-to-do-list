# Contains app logic for user interaction within the terminal interface
import models

class App():
    '''Will utilize ToDoList class to define user interactions.'''

    def __init__(self):
        self.toDoList = models.ToDoList() # create new to do list object

    def read_input(self):
        '''Prompts and parses user input. Returns int corresponding to command.'''
        user_input = input("Enter command: ")
        # Parse user input
        user_input_split = user_input.split()
        user_command = user_input_split[0]
        user_item  = user_input_split[-1]

        # Handle invalid input
        valid_commands = ["add", "finish", "delete", "quit"]
        if len(user_input_split) > 2 or user_command.lower() not in valid_commands:
            # invalid if too many arguments or unrecognized command
            print("Invalid command.")

        # Read command

        match user_command:
            case "add":
                return 0
            case "finish":
                return 1
            case "delete":
                return 2
            case "quit":
                return 3
            case _:
                return -1





    