import json

"""
Function parse input takes a string and returns a tuple
with the command and the arguments.

"""
def parse_input(user_input):
    cmd, *args =  user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

"""
Function add_contact takes a list of arguments and a dictionary
Block 'If' checks if the length of the arguments is not equal to 2
and raises a ValueError with the message "Command format is add [name] [phone]"
"""
def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Command format is add [name] [phone]")
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as ve:
        return str(ve)

"""
Function show_contacts takes a dictionary and an optional name argument,
If the dictionary is empty, it returns the message "No contacts to show."
If the name is provided, it returns the name and the phone number
"""

def show_contacts(contacts, name = None):
    if not contacts:
        return "No contacts to show."
    if name:
        return f"{name}: {contacts.get(name, 'Not found')}"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

"""
Function save_contacts saving the contacts to a file, with availability to load 
the saved contacts during next program start.
"""
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file)

"""
Function load_contacts loads the contacts from a file, if the file is not found
it returns an empty dictionary with error message.
"""
def load_contacts(filename = "contacts.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}
    
"""
Function change_contacts takes a dictionary, a name, and a phone number.
It updates the contact with the given name to the new phone number.
"""
def change_contacts(contacts, name, phone):
    contacts[name] = phone
    return "Contact changed."

"""
Main function block, where the program starts.
It loads the contacts, prints a welcome message, and enters a loop
to read user input and execute commands.
The loop breaks when the user enters "close" or "exit".
It saves the contacts before exiting.
"""
def main():
    contacts = load_contacts()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_contacts(contacts)
            print("Good bye!")
            break
        elif command in ["hello","hi", "hey"]:
            print("Hi, how can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contacts(contacts, args[0], args[1]))
        elif command == "show":
            if args:
                print(show_contacts(contacts, args[0]))
            else:
                print(show_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
