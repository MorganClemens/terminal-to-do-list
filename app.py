# app.py
import models

def main():
    # Build new todolist object
    new_list = models.ToDoList()

    # For Testing
    new_list.add_item("Build resin holder")
    new_list.add_item("Go surfing")
    new_list.add_item("Pack lunch for later")

    new_list.print_list()

    new_list.finish_item("Build resin holder")

    new_list.print_list()

if __name__ == "__main__":
    main()