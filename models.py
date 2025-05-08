# Contains functions and helper functions.

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
