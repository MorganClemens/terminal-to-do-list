# Terminal To-Do List App

This is a simple command-line To-Do List application written in Python. It allows users to add, complete, and remove tasks using a clean and intuitive terminal interface. The project is structured to promote modularity and clarity, making it a great starting point for beginners learning Python, object-oriented programming, and command-line interaction.

## Features

- Add new items to your to-do list  
- Mark items as completed  
- Remove items from the list  
- View your active and finished tasks  
- Runs entirely in the terminal  
- Clears the screen after each command for a clean view

## File Structure

```
.
├── models.py      # Defines the ToDoList class and its core functions
├── app.py         # Manages user interaction and command execution
├── main.py        # Entry point that runs the main application loop
```

## How to Run

1. Clone or download the repository.

2. In the terminal, navigate to the project directory and run:

```
python main.py
```

3. Follow the on-screen instructions to interact with your to-do list.

## Commands

Type commands in the following format (case-sensitive):

- `add laundry` — Add "laundry" to your list  
- `finish laundry` — Mark "laundry" as completed  
- `remove laundry` — Remove "laundry" from the list  
- `quit` — Exit the application

## Requirements

- Python 3.x  
- No additional libraries required

## Sample Output

```
To-Do List
------------------------
✓ read book
☐ laundry
☐ write code


add 'item' to add.
finish 'item' to check off list.
remove 'item' to delete item.
'quit' to quit.

Enter command:
```
