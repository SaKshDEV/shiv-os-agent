
from datetime import datetime


def normalize_voice_command(text):
    text = text.strip().lower()

    voice_commands = {
        "नमस्ते": "hello",
        "हेलो": "hello",
        "टाइम": "time",
        "समय": "time",
        "समय बताओ": "time",
        "समय बता": "time",
        "अभी का समय बताओ": "time",
        "मुझे अभी का समय बताओ": "time",
        "अभी का टाइम बताओ": "time",
        "भाई अभी का टाइम बता": "time",
        "bhai abhi ka time bata": "time",
        "abhi ka time bata": "time",
        "bhai time bata": "time",
        "time bata": "time",
        "what time is it": "time",
        "मदद": "help",
        "नाम बदल दो": "change name",
        "मेरा नाम बदल दो": "change name",
        "नाम भूल जा": "forget name",
        "मेरा नाम भूल जा": "forget name",
        "बंद हो जाओ": "exit",
        "बाहर निकलो": "exit",
        "नोटपैड खोलो": "open notepad",
        "नोटपैड खोल दो": "open notepad",
        "notepad kholo": "open notepad",
        "notepad khol do": "open notepad",
        "नोट पैड खोलो": "open notepad",
        "नोट पैड खोल दो": "open notepad",
        "कैलकुलेटर खोलो": "open calculator",
        "कैलकुलेटर खोल दो": "open calculator",
        "calculator kholo": "open calculator",
        "calculator khol do": "open calculator",

    }

    for phrase, command in voice_commands.items():
        if phrase in text:
            return command

    return text



COMMAND_INTENTS = {
    "hello": "greet",
    "change name": "change_name",
    "mera naam badal do": "change_name",
    "naam badal do": "change_name",
    "forget name": "forget_name",
    "naam bhool ja": "forget_name",
    "mera naam bhool ja": "forget_name",
    "help": "help",
    "time": "get_time",
    "exit": "exit",
    "open notepad": "open_notepad",
    "open calculator": "open_calculator",
}

def detect_intent(command):
    command = command.strip().lower()
    return COMMAND_INTENTS.get(command, "unknown")


def process_intent(intent, user_name):
    if intent == "greet":
        if user_name:
            return f"Hey {user_name} bhai! Kaisa hai?"
        return "Hey bhai! Kaisa hai?"

    elif intent == "change_name":
        return "CHANGE_NAME"

    elif intent == "forget_name":
        return "FORGET_NAME"

    elif intent == "help":
        return (
            "Commands: hello, help, time, "
            "change name, forget name, exit"
        )

    elif intent == "open_notepad":
        return "OPEN_NOTEPAD"

    elif intent == "open_calculator":
        return "OPEN_CALCULATOR"        

    elif intent == "get_time":
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Abhi time hai {current_time}"

    elif intent == "exit":
        return "EXIT"

    else:
        return "Ye command abhi samajh nahi aayi."


def process_command(command, user_name):
    intent = detect_intent(command)
    return process_intent(intent, user_name)

