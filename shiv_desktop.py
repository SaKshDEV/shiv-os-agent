import subprocess

APPLICATION = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
}

def open_application(app_name):
    app_name = app_name.strip().lower()

    command = APPLICATION.get(app_name)

    if command is None:
        return False, f"'{app_name}' approved applications mein nhi hai."

    try:
        subprocess.Popen(command)

    except OSError:
        return False, f"{app_name} open nahi ho paaya."

    return True, f"{app_name.title()} open ho gaya!"            