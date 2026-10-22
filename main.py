from shiv_brain import process_command

def main():
    print("================================")
    print("SHIV OS")
    print("Your personal AI companion")
    print("Foundation module initialized.")
    print("================================")

    user_name = input("SHIV: pehle apna naam bata bhai:")
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
