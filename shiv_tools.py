from shiv_desktop import open_application

TOOLS = {
    "notepad": lambda: open_application("notepad"),
    "calculator": lambda: open_application("calculator"),

}

def execute_tool(tool_name):
    tool_name = tool_name.strip().lower()

    tool = TOOLS.get(tool_name)

    if tool is None:
        return False, f"`{tool_name}` is not an approved tool"

    try:
        return tool()
    except Exception:
        return False, f"Tool '{tool_name}' failed to execute."
