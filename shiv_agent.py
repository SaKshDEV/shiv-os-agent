from dataclasses import dataclass

from shiv_brain import normalize_voice_command, process_command


@dataclass(frozen=True)
class AgentResult:
    kind: str
    value: str = ""


def interpret_request(text, user_name):
    command = normalize_voice_command(text)
    response = process_command(command, user_name)

    if response == "OPEN_NOTEPAD":
        return AgentResult(kind="action", value="notepad")

    if response == "OPEN_CALCULATOR":
        return AgentResult(kind="action", value="calculator")

    if response == "CHANGE_NAME":
        return AgentResult(kind="control", value="change_name")

    if response == "FORGET_NAME":
        return AgentResult(kind="control", value="forget_name")

    if response == "EXIT":
        return AgentResult(kind="control", value="exit")

    return AgentResult(kind="reply", value=response)