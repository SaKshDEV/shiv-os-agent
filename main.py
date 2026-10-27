from shiv_memory import load_memory, save_memory
from shiv_brain import process_command, normalize_voice_command
from shiv_voice import listen_once
from shiv_desktop import open_application
from shiv_speech import speak


def shiv_reply(message):
    print(f"SHIV: {message}")

    try:
        speak(message)
    except Exception as error:
        print(f"SHIV: Voice output nahi chal paaya: {error}")


def main():
    print("================================")
    print("SHIV OS")
    print("Your personal AI companion")
    print("Foundation module initialized.")
    print("================================")

    memory = load_memory()
    user_name = memory.get("user_name", "")

    if not user_name:
        shiv_reply("Tera naam kya hai bhai?")
        user_name = input("YOU: ").strip()

    if user_name:
        memory["user_name"] = user_name
        save_memory(memory)

    shiv_reply(f"Har Har Mahadev, {user_name}!")

    while True:
        command = input("\nYOU: ").strip().lower()

        if command == "voice":
            try:
                recognized_text = listen_once()
            except Exception as error:
                print(f"SHIV: Voice input mein problem aayi: {error}")
                continue

            if not recognized_text:
                shiv_reply("Kuch sunai nahi diya. Dobara try kar.")
                continue

            print(f"YOU (voice): {recognized_text}")
            command = recognized_text

        command = normalize_voice_command(command)
        response = process_command(command, user_name)

        if response == "OPEN_NOTEPAD":
            success, message = open_application("notepad")
            shiv_reply(message)
            continue

        elif response == "OPEN_CALCULATOR":
            success, message = open_application("calculator")
            shiv_reply(message)
            continue

        if response == "CHANGE_NAME":
            shiv_reply("Naya naam kya rakhu bhai?")
            new_name = input("YOU: ").strip()

            if new_name:
                user_name = new_name
                memory["user_name"] = user_name
                save_memory(memory)
                shiv_reply(
                    f"Samajh gaya bhai, ab tujhe {user_name} bulaunga!"
                )
            else:
                shiv_reply("Naam khali nahi ho sakta.")

            continue

        elif response == "FORGET_NAME":
            memory.pop("user_name", None)
            save_memory(memory)
            user_name = ""
            shiv_reply("Tera naam saved memory se delete kar diya.")
            continue

        if response == "EXIT":
            shiv_reply("Theek hai bhai, milte hain phir!")
            break

        shiv_reply(response)


if __name__ == "__main__":
    main()