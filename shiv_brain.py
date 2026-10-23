
from datetime import datetime


def process_command(command, user_name):
    if command == "hello":
        if user_name:
            return f"Hey {user_name} bhai! kaisa hai?"
        return "Hey bhai! kaisa hai"
    elif command == "change name":
        return "CHANGE_NAME"
    elif command == "forget name":
        return "FORGET_NAME"

    elif command == "help":
        return "Commands: hello, help, time, exit"

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Abhi time hai {current_time}"

    elif command == "exit":
        return "EXIT"

    else:
        return "Ye command abhi samajh nahi aayi."
