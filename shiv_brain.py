
from datetime import datetime


def process_command(command, user_name):
    if command == "hello":
        return f"Hey {user_name} bhai! kaisa hai?"

    elif command == "help":
        return "Commands: hello, help, time, exit"

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Abhi time hai {current_time}"

    elif command == "exit":
        return "EXIT"

    else:
        return "Ye command abhi samajh nahi aayi."
