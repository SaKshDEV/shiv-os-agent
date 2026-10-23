
from datetime import datetime


def normalize_voice_command(text):
    text = text.strip().lower()

    voice_commands = {
        "नमस्ते": "hello",
        "हेलो": "hello",
        "टाइम": "time",
        "समय": "time",
        "मदद": "help",
        "नाम बदल दो": "change name",
        "मेरा नाम बदल दो": "change name",
        "नाम भूल जा": "forget name",
        "मेरा नाम भूल जा": "forget name",
        "बंद हो जाओ": "exit",
        "बाहर निकलो": "exit",
    }

    for phrase, command in voice_commands.items():
        if phrase in text:
            return command

    return text


def process_command(command, user_name):
    if command == "hello":
        if user_name:
            return f"Hey {user_name} bhai! Kaisa hai?"
        return "Hey bhai! Kaisa hai?"

    elif command in (
        "change name", "mera naam badal do", "naam badal do"
    ):
        return "CHANGE_NAME"

    elif command in (
        "forget name", "naam bhool ja", "mera naam bhool ja"
    ):
        return "FORGET_NAME"

    elif command == "help":
        return "Commands: hello, help, time, change name, forget name, exit"

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Abhi time hai {current_time}"

    elif command == "exit":
        return "EXIT"

    else:
        return "Ye command abhi samajh nahi aayi."
