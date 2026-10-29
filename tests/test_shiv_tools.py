import unittest
from unittest.mock import patch

from shiv_tools import execute_tool


class TestShivTools(unittest.TestCase):

    @patch(
        "shiv_tools.open_application",
        return_value=(True, "Notepad open ho gaya!"),
    )
    def test_notepad_tool(self, mock_open):
        success, message = execute_tool("notepad")

        self.assertTrue(success)
        self.assertEqual(message, "Notepad open ho gaya!")
        mock_open.assert_called_once_with("notepad")

    @patch(
        "shiv_tools.open_application",
        return_value=(True, "Calculator open ho gaya!"),
    )
    def test_calculator_tool(self, mock_open):
        success, message = execute_tool("calculator")

        self.assertTrue(success)
        self.assertEqual(message, "Calculator open ho gaya!")
        mock_open.assert_called_once_with("calculator")

    @patch("shiv_tools.open_application")
    def test_unknown_tool_is_rejected(self, mock_open):
        success, message = execute_tool("delete_everything")

        self.assertFalse(success)
        self.assertIn("not an approved tool", message)
        mock_open.assert_not_called()

    @patch(
        "shiv_tools.open_application",
        return_value=(True, "Notepad open ho gaya!"),
    )
    def test_tool_name_is_normalized(self, mock_open):
        success, message = execute_tool("  NOTEPAD  ")

        self.assertTrue(success)
        mock_open.assert_called_once_with("notepad")

    @patch(
        "shiv_tools.open_application",
        side_effect=OSError("Launch failed"),
    )
    def test_tool_error_is_handled(self, mock_open):
        success, message = execute_tool("notepad")

        self.assertFalse(success)
        self.assertEqual(
            message,
            "Tool 'notepad' failed to execute.",
        )


if __name__ == "__main__":
    unittest.main()