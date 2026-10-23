from shiv_memory import load_memory,save_memory
from shiv_brain import process_command

def main():
    print("================================")
    print("SHIV OS")
    print("Your personal AI companion")
    print("Foundation module initialized.")
    print("================================")

    memory = load_memory()
    user_name = memory.get("user_name","")

    if not user_name:
        user_name = input("SHIV:Tera naam kya hai bhai?").strip()

    if user_name:
        memory["user_name"] = user_name
        save_memory(memory)

    print(f"SHIV: Har Har Mahadev,{user_name}!")

    while True:
        command = input("\nyou: ").strip().lower()

        response = process_command(command,user_name)

        if response == "EXIT":
            print("SHIV: theek hai bhai, milte hain phir")
            break 
                 
        print(f"SHIV: {response}")
if __name__ == "__main__":
    main()
