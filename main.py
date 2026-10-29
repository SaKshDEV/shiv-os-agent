from shiv_memory import load_memory, save_memory
from shiv_agent import interpret_request
from shiv_voice import listen_once
from shiv_tools import execute_tool
from shiv_speech import speak, to_hindi_speech_text


def shiv_reply(message):
    speech_text = to_hindi_speech_text(message)

    print(f"SHIV: {speech_text}")

    try:
        speak(speech_text)
    except Exception as error:
        print(f"SHIV: Voice output nahi chal paaya: {error}")


def main():
    print("================================")
    print("SHIV OS")
    print("Your personal AI companion")
    print("Agent Core initialized.")
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

        result = interpret_request(command, user_name)

        if result.kind == "action":
            success, message = execute_tool(result.value)
            shiv_reply(message)
            continue

        if result.kind == "control":

            if result.value == "change_name":
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

            if result.value == "forget_name":
                memory.pop("user_name", None)
                save_memory(memory)
                user_name = ""
                shiv_reply("Tera naam saved memory se delete kar diya.")
                continue

            if result.value == "exit":
                shiv_reply("Theek hai bhai, milte hain phir!")
                break

        if result.kind == "reply":
            shiv_reply(result.value)


if __name__ == "__main__":
    main()