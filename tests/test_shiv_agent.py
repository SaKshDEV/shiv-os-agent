import unittest
from unittest.mock import patch

from shiv_agent import interpret_request


class TestShivAgent(unittest.TestCase):

    @patch("shiv_agent.process_command")
    @patch("shiv_agent.normalize_voice_command")
    def test_time_request_returns_reply(
        self, mock_normalize, mock_process
    ):
        mock_normalize.return_value = "time"
        mock_process.return_value = "It is 9 PM"

        result = interpret_request("time", "Saksham")

        self.assertEqual(result.kind, "reply")
        self.assertEqual(result.value, "It is 9 PM")

    @patch("shiv_agent.process_command")
    @patch("shiv_agent.normalize_voice_command")
    def test_notepad_request_returns_action(
        self, mock_normalize, mock_process
    ):
        mock_normalize.return_value = "open notepad"
        mock_process.return_value = "OPEN_NOTEPAD"

        result = interpret_request("open notepad", "Saksham")

        self.assertEqual(result.kind, "action")
        self.assertEqual(result.value, "notepad")

    @patch("shiv_agent.process_command")
    @patch("shiv_agent.normalize_voice_command")
    def test_calculator_request_returns_action(
        self, mock_normalize, mock_process
    ):
        mock_normalize.return_value = "open calculator"
        mock_process.return_value = "OPEN_CALCULATOR"

        result = interpret_request("open calculator", "Saksham")

        self.assertEqual(result.kind, "action")
        self.assertEqual(result.value, "calculator")

    @patch("shiv_agent.process_command")
    @patch("shiv_agent.normalize_voice_command")
    def test_exit_returns_control(
        self, mock_normalize, mock_process
    ):
        mock_normalize.return_value = "exit"
        mock_process.return_value = "EXIT"

        result = interpret_request("exit", "Saksham")

        self.assertEqual(result.kind, "control")
        self.assertEqual(result.value, "exit")

    def test_agent_result_is_immutable(self):
        from shiv_agent import AgentResult

        result = AgentResult(kind="reply", value="Hello")

        with self.assertRaises(AttributeError):
            result.value = "Changed"


if __name__ == "__main__":
    unittest.main()