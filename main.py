import app

def main():
    current_session = app.App() # Create an instance of App

    
    while True:
        try:
            current_session.toDoList.print_list() # display current list state
            for code in current_session.error_codes: print(code) # print error codes
            current_session.error_codes.clear() # clear codes for next loop
            command_index = current_session.read_input() # get user command

            current_session.execute_command(command_index) # perform user command

        except ValueError as e:
            print(f"Value error: {e}")
        except IndexError:
            print("That item wasn't found in the list.")
        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()