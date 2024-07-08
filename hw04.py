def parse_input(user_input):
    """
    Separating string input from user to command and args.
    Args: 
        user_input(str): input from user
    Returns:
        tuple: Command and list of args. 
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

    
    
def add_contact(args, contacts):
    """
    Adds new contact to contact dict.
    args list:
        name, phone
    Returns:
        str: Message regarding programm completion.
    """
    try:
        if len(args) != 2:
            raise ValueError("Error: Command format is 'add [name] [phone]'")
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as ve:
        return str(ve)


        
def change_contact(args, contacts):
    """
    Changes a telephone number for existing contact.
    args list:
        name, phone
    Returns:
        str: Message regarding programm completion.
    """
    try:
        if len(args) != 2:
            raise ValueError("Error: Command format is 'change [name] [new phone]'")
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Error: Contact not found."
    except ValueError as ve:
        return str(ve)



def show_phone(args, contacts):
    """
    Shows telephone number for selected contact.
    args list: 
        name, contacts
    Returns: 
        str: Telephone number or error message.
    """
    try:
        if len(args) != 1:
            raise ValueError("Error: Command format is 'phone [name]'")
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Error: Contact not found."
    except ValueError as ve:
        return str(ve)

def show_all(contacts):
    """
    Shows all saved telephone numbers.
    args: 
        contacts (type = dict)
    Returns: 
        str: All contacts list or error message of missing contacts.
    """
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    """
    Main cycle of programm, processing user inputs and calling a specified functions.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except Exception as e:
            print("Your input was empty or invalid, please try again.")

if __name__ == "__main__":
    main()
