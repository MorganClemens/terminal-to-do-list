# Contains functions and helper functions.

import os # for clearing the console

class ToDoList:
    '''Creates a new to-do list object.'''

    def __init__(self):
        self.todo = []
        self.finished = []

    def add_item(self, item):
        '''Appends an item to the to-do list.'''
        self.todo.append(item)

    def finish_item(self, item):
        '''Moves item from to-do list to finished list.'''
        finished_index = self.todo.index(item)
        finished_item = self.todo.pop(finished_index)
        self.finished.append(finished_item)

    def remove_item(self, item):
        '''Deletes item from to-do list without finishing.'''
        if item in self.todo:
            self.todo.remove(item)
        elif item in self.finished:
            self.finished.remove(item)
        else:
            return
        
    def print_list(self):
        '''Displays the list to the user.'''
        # Clear the console
        self.clear_console()
        # Print top header
        print("To-Do List\n------------------------")
        # Print finished list
        for item in self.finished:
            print('\u2713' + " " + item)
        # Print todo list
        for item in self.todo:
            print('\u2610' + " " + item)
        # Print user commands
        print("\n\nadd 'item' to add.\n"
              "finish 'item' to check off list.\n"
              "remove 'item' to delete item.\n"
              "'quit' to quit.")
        
    def clear_console(self):
        '''Clears the console.'''
        os.system('cls' if os.name == 'nt' else 'clear')